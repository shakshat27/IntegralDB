# IntegralDB

A retrieval-augmented (RAG) knowledge base for supplier documents: pricing sheets and technical specs are pulled from Google Drive, embedded into Postgres with pgvector, and answered in plain language through a Streamlit chat with sources.

<!-- screenshot: docs/chat.png -->

## Features

- **Drive ingestion**: reads the `Commercial` (pricing) and `Technical` (specs) folders, PDFs and Google Docs, exports Docs to PDF
- **Incremental**: skips files already in the database
- **Chunking + embeddings**: 1,000-character chunks with 200 overlap, Gemini embeddings, stored with category tag and source file in Supabase (`company_knowledge`)
- **Chat interface**: question → embedding → `match_documents` similarity search → Gemini 2.5 Flash answers **only from the retrieved context** and cites the source files
- Falls back to a clearly labelled general answer when nothing relevant is found
- `clear_database.py`: confirmed wipe of tables for a fresh re-ingest

## Architecture

```
Google Drive (Commercial/, Technical/)
        │  Drive API (OAuth)
        ▼
unified_ingest.py ── pdfplumber → chunks → Gemini embeddings ──► Supabase Postgres + pgvector
                                                                       │ match_documents()
app.py (Streamlit chat) ── query embedding ────────────────────────────┘
        │ top-5 chunks as context
        ▼
Gemini 2.5 Flash → answer with sources
```

## Tech stack

Python · Streamlit · Google Gemini (embeddings + 2.5 Flash) · Supabase (Postgres, pgvector) · Google Drive API · pdfplumber

## Setup

```bash
pip install -r requirements.txt streamlit
```

`.env` (or Streamlit secrets):

```
GOOGLE_API_KEY=...
SUPABASE_URL=...
SUPABASE_KEY=...
```

Supabase: enable `pgvector`, create the `company_knowledge` table (content, embedding, category, source_filename) and a `match_documents(query_embedding, match_threshold, match_count)` function. Google Cloud: an OAuth client `credentials.json` with Drive read access.

```bash
python unified_ingest.py     # ingest Drive folders
streamlit run app.py         # chat
```

## Structure

| file | role |
|---|---|
| `unified_ingest.py` | Drive → text → chunks → embeddings → Supabase |
| `app.py` | Streamlit RAG chat |
| `clear_database.py` | wipe tables (asks for confirmation) |

## License

Proprietary - All Rights Reserved
