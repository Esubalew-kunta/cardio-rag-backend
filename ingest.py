"""
ingest.py — Cardio Check-up RAG knowledge base ingestion.

Reads DOC_01–DOC_06 from knowledge_base/, splits each file into chunks by
"## " heading, embeds every chunk locally with all-MiniLM-L6-v2, and uploads
them to a Qdrant Cloud collection. DOC_07 is the system prompt and is NOT
ingested.

Setup:
    pip install fastembed qdrant-client python-dotenv tqdm
    cp .env.example .env   # then fill in QDRANT_URL and QDRANT_API_KEY

Run:
    python ingest.py
"""

import os
import re
import sys
import uuid
import glob
import traceback

from dotenv import load_dotenv

# Progress indicator with graceful fallback if tqdm is not installed.
try:
    from tqdm import tqdm
except ImportError:  # pragma: no cover
    def tqdm(iterable, **kwargs):
        return iterable

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------
KB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knowledge_base")
COLLECTION_NAME = "cardio_checkup_kb"
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # fastembed model id
VECTOR_SIZE = 384  # all-MiniLM-L6-v2 output dimension
# Only these six documents go into Qdrant. DOC_07 (system prompt) is excluded.
INGEST_GLOB = "DOC_0[1-6]_*.md"

# Stable UUID namespace so re-ingesting the same chunk_id yields the same point id.
UUID_NAMESPACE = uuid.UUID("00000000-0000-0000-0000-00000000ca12")


# ----------------------------------------------------------------------------
# Parsing
# ----------------------------------------------------------------------------
def source_doc_from_filename(path):
    """DOC_01_practice_overview.md -> 'DOC_01'."""
    m = re.search(r"(DOC_0\d)", os.path.basename(path))
    return m.group(1) if m else os.path.basename(path)


def parse_file(path):
    """Split one markdown file into chunks by level-2 (## ) headings.

    Returns a list of dicts: {chunk_id, source_doc, section_number,
    language, title, text}. Skips the file preamble and any trailing
    meta sections (### Open flags, ### Flag summary, etc.). Keeps the
    in-chunk ### FR / ### EN sub-headings used by DOC_04.
    """
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()

    source_doc = source_doc_from_filename(path)

    # Split on level-2 headings only ("## "), never ### or #.
    parts = re.split(r"(?m)^##\s+", content)[1:]  # drop file preamble

    chunks = []
    for raw in parts:
        lines = raw.splitlines()
        if not lines:
            continue
        heading = lines[0].strip()
        body_lines = lines[1:]

        # A real chunk carries a `chunk_id:` metadata line. Skip anything else.
        meta_line = next((ln for ln in body_lines if "chunk_id:" in ln), None)
        if not meta_line:
            continue

        cid_match = re.search(r"chunk_id:\s*([A-Za-z0-9_]+)", meta_line)
        if not cid_match:
            continue
        chunk_id = cid_match.group(1)

        lang_match = re.search(r"lang:\s*([a-z,]+)", meta_line)
        language = lang_match.group(1) if lang_match else "fr,en"

        sec_match = re.match(r"(\d+\.\d+[a-z]?)", heading)
        section_number = sec_match.group(1) if sec_match else ""

        # Rebuild the body: drop the metadata line, stop at any trailing
        # meta section heading (a ### that is not FR/EN).
        kept = []
        meta_removed = False
        for ln in body_lines:
            if not meta_removed and "chunk_id:" in ln:
                meta_removed = True
                continue
            h3 = re.match(r"^###\s+(.*)", ln)
            if h3 and h3.group(1).strip() not in ("FR", "EN"):
                break
            kept.append(ln)

        body = "\n".join(kept).strip()
        body = re.sub(r"\n?-{3,}\s*$", "", body).strip()  # strip trailing rule

        text = (heading + "\n" + body).strip()
        if not text:
            continue

        chunks.append(
            {
                "chunk_id": chunk_id,
                "source_doc": source_doc,
                "section_number": section_number,
                "language": language,
                "title": heading,
                "text": text,
            }
        )

    return chunks


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main():
    load_dotenv()

    qdrant_url = os.getenv("QDRANT_URL")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")
    if not qdrant_url or not qdrant_api_key:
        print("ERROR: QDRANT_URL and QDRANT_API_KEY must be set in your .env file.")
        sys.exit(1)

    if not os.path.isdir(KB_DIR):
        print(f"ERROR: knowledge_base folder not found at {KB_DIR}")
        sys.exit(1)

    # Imported here so missing deps give a clear message before heavy work.
    from fastembed import TextEmbedding
    from qdrant_client import QdrantClient
    from qdrant_client.models import Distance, VectorParams, PointStruct

    # --- 1. READ + 2. SPLIT ------------------------------------------------
    files = sorted(glob.glob(os.path.join(KB_DIR, INGEST_GLOB)))
    if not files:
        print(f"ERROR: no DOC_01–DOC_06 markdown files found in {KB_DIR}")
        sys.exit(1)

    all_chunks = []
    per_doc_counts = {}
    print("Reading and splitting knowledge base files:")
    for path in files:
        chunks = parse_file(path)
        src = source_doc_from_filename(path)
        per_doc_counts[src] = len(chunks)
        all_chunks.extend(chunks)
        print(f"  {os.path.basename(path):42s} -> {len(chunks):2d} chunks")
    print(f"  Total: {len(all_chunks)} chunks\n")

    # --- 3. EMBED ----------------------------------------------------------
    print(f"Loading embedding model '{EMBED_MODEL_NAME}' (first run downloads it)...")
    model = TextEmbedding(model_name=EMBED_MODEL_NAME)

    points = []
    failed = []  # (chunk_id, reason)
    print("Embedding chunks:")
    for ch in tqdm(all_chunks, desc="  embedding", unit="chunk"):
        try:
            # fastembed returns a generator of numpy arrays (normalized).
            vector = list(model.embed([ch["text"]]))[0].tolist()
            point_id = str(uuid.uuid5(UUID_NAMESPACE, ch["chunk_id"]))
            points.append(
                PointStruct(
                    id=point_id,
                    vector=vector,
                    payload={
                        "chunk_id": ch["chunk_id"],
                        "source_doc": ch["source_doc"],
                        "section_number": ch["section_number"],
                        "language": ch["language"],
                        "title": ch["title"],
                        "text": ch["text"],
                    },
                )
            )
        except Exception as exc:  # log and continue, never crash
            failed.append((ch.get("chunk_id", "<unknown>"), repr(exc)))
            print(f"    FAILED to embed {ch.get('chunk_id', '<unknown>')}: {exc}")

    # --- 4. UPLOAD ---------------------------------------------------------
    print("\nConnecting to Qdrant Cloud...")
    client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key, timeout=60)

    # Clean re-ingest: delete the collection if it exists, then recreate.
    try:
        if client.collection_exists(COLLECTION_NAME):
            print(f"Collection '{COLLECTION_NAME}' exists — deleting for clean re-ingest.")
            client.delete_collection(COLLECTION_NAME)
    except Exception as exc:
        # Older clients may lack collection_exists; fall back to a best-effort delete.
        try:
            client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass
        print(f"  (note: existence check fallback used: {exc})")

    print(f"Creating collection '{COLLECTION_NAME}' (size={VECTOR_SIZE}, distance=Cosine).")
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
    )

    print("Uploading points:")
    uploaded = 0
    BATCH = 64
    for i in tqdm(range(0, len(points), BATCH), desc="  upserting", unit="batch"):
        batch = points[i : i + BATCH]
        try:
            client.upsert(collection_name=COLLECTION_NAME, points=batch)
            uploaded += len(batch)
        except Exception as exc:
            # Batch failed — retry each point individually so one bad point
            # does not lose the whole batch.
            print(f"    Batch {i // BATCH} failed ({exc}); retrying point by point.")
            for p in batch:
                try:
                    client.upsert(collection_name=COLLECTION_NAME, points=[p])
                    uploaded += 1
                except Exception as exc2:
                    cid = p.payload.get("chunk_id", "<unknown>")
                    failed.append((cid, f"upsert: {exc2!r}"))
                    print(f"      FAILED to upload {cid}: {exc2}")

    # --- 5. SUMMARY --------------------------------------------------------
    print("\n" + "=" * 60)
    print("INGESTION SUMMARY")
    print("=" * 60)
    print(f"Total chunks processed : {len(all_chunks)}")
    print("Chunks per document    :")
    for doc in sorted(per_doc_counts):
        print(f"    {doc} : {per_doc_counts[doc]}")
    print(f"Embedded successfully  : {len(points)}")
    print(f"Uploaded to Qdrant     : {uploaded}")
    if failed:
        print(f"Failed chunks          : {len(failed)}")
        for cid, reason in failed:
            print(f"    - {cid}: {reason}")
    else:
        print("Failed chunks          : 0")
    print("=" * 60)
    print("Ingestion complete.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(1)
    except Exception:
        print("\nFatal error during ingestion:")
        traceback.print_exc()
        sys.exit(1)
