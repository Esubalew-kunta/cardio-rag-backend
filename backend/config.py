"""
config.py — central configuration for the Cardio Check-up RAG backend.

Everything that must stay in sync with ingest.py lives here (collection name,
embedding model, vector space). All secrets come from the environment (.env);
nothing is hardcoded.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# --- Paths ------------------------------------------------------------------
# backend/ is a sibling of knowledge_base/ inside the project root.
BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BACKEND_DIR)
KB_DIR = os.path.join(PROJECT_ROOT, "knowledge_base")
SYSTEM_PROMPT_PATH = os.path.join(KB_DIR, "DOC_07_system_prompt.md")

# --- Must match ingest.py ---------------------------------------------------
COLLECTION_NAME = "cardio_checkup_kb"
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # fastembed model id
VECTOR_SIZE = 384

# --- Retrieval tuning -------------------------------------------------------
TOP_K = int(os.getenv("RAG_TOP_K", "4"))
# Cosine similarity floor; chunks below this are treated as irrelevant.
SIMILARITY_THRESHOLD = float(os.getenv("RAG_SCORE_THRESHOLD", "0.30"))

# --- Claude -----------------------------------------------------------------
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")
CLAUDE_MAX_TOKENS = int(os.getenv("CLAUDE_MAX_TOKENS", "1024"))
CLAUDE_TEMPERATURE = 0.0  # factual, never creative — non-negotiable

# --- Secrets (from .env) ----------------------------------------------------
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")


def require_secrets():
    """Fail fast at startup if any required secret is missing."""
    missing = [
        name
        for name, value in (
            ("QDRANT_URL", QDRANT_URL),
            ("QDRANT_API_KEY", QDRANT_API_KEY),
            ("CLAUDE_API_KEY", CLAUDE_API_KEY),
        )
        if not value
    ]
    if missing:
        raise RuntimeError(
            "Missing required environment variables: "
            + ", ".join(missing)
            + ". Copy .env.example to .env and fill them in."
        )
