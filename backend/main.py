"""
main.py — FastAPI backend for the Cardio Check-up RAG chat agent.

Flow per request:
  patient message -> embed -> Qdrant top-K search (above threshold)
  -> DOC_07 system prompt + retrieved context + conversation history
  -> Claude (Sonnet 4.6, temperature 0) -> SSE stream back to the frontend.

The embedding model, Qdrant client, Anthropic client and DOC_07 system prompt
are loaded once at startup (lifespan), never per request.
"""

import json
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from typing import List

import config
import rag


# ----------------------------------------------------------------------------
# Request schema
# ----------------------------------------------------------------------------
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


# ----------------------------------------------------------------------------
# Startup / shutdown — load everything once
# ----------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    config.require_secrets()

    # Heavy imports kept here so a missing dependency surfaces clearly.
    from fastembed import TextEmbedding
    from qdrant_client import QdrantClient
    from anthropic import Anthropic

    print(f"Loading embedding model '{config.EMBED_MODEL_NAME}'...")
    app.state.model = TextEmbedding(model_name=config.EMBED_MODEL_NAME)

    print("Connecting to Qdrant Cloud...")
    app.state.qdrant = QdrantClient(
        url=config.QDRANT_URL,
        api_key=config.QDRANT_API_KEY,
        timeout=30,
        check_compatibility=False,
    )

    print("Initialising Anthropic client...")
    app.state.anthropic = Anthropic(api_key=config.CLAUDE_API_KEY)

    print("Loading DOC_07 system prompt...")
    with open(config.SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as fh:
        app.state.system_prompt = fh.read()

    print("Startup complete. Backend ready.")
    yield
    # nothing to clean up explicitly


app = FastAPI(title="Cardio Check-up RAG Agent", lifespan=lifespan)

# CORS — open for now so the React frontend can reach it.
# TODO: restrict allow_origins to the production domain before launch.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------------------------------------------------------------------------
# Health check (for Render)
# ----------------------------------------------------------------------------
@app.get("/health")
async def health():
    return {"status": "ok"}


# ----------------------------------------------------------------------------
# Chat — Retrieval Augmented Generation, streamed over SSE
# ----------------------------------------------------------------------------
def _sse(event: dict) -> str:
    """Serialize one Server-Sent-Events frame."""
    return f"data: {json.dumps(event, ensure_ascii=False)}\n\n"


@app.post("/chat")
async def chat(req: ChatRequest, request: Request):
    messages = rag.sanitize_messages([m.model_dump() for m in req.messages])
    if not messages:
        return JSONResponse(
            status_code=400,
            content={"error": "No valid user message in the conversation."},
        )

    query = rag.last_user_message(messages)
    if not query:
        return JSONResponse(
            status_code=400,
            content={"error": "The latest turn must contain a user message."},
        )

    model = request.app.state.model
    qdrant = request.app.state.qdrant
    anthropic_client = request.app.state.anthropic
    doc07 = request.app.state.system_prompt

    def event_stream():
        try:
            # 1. retrieve grounding context for the latest patient message
            vector = rag.embed_query(model, query)
            hits = rag.search_chunks(qdrant, vector)
            context = rag.build_context(hits)
            system_prompt = rag.build_system_prompt(doc07, context)

            # 2. stream Claude's answer back token by token
            for text in rag.stream_claude(anthropic_client, system_prompt, messages):
                yield _sse({"type": "delta", "text": text})

            yield _sse({"type": "done"})
        except Exception as exc:  # never leak a stack trace to the patient
            print(f"[/chat] error: {exc!r}")
            yield _sse(
                {
                    "type": "error",
                    "message": "Une erreur est survenue. Veuillez réessayer ou "
                    "contacter le secrétariat au 07 55 50 52 58.",
                }
            )

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",  # disable proxy buffering (e.g. on Render)
        },
    )
