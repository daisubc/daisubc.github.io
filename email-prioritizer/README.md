# 📥 Inbox Triage — Email Summarizer & Prioritizer

A small web app that reads your Gmail, **summarizes each email** and **ranks
your inbox by priority** using an open-source LLM. Built to deploy with the
frontend on **Vercel** and the backend on **Render**.

```
┌──────────────┐   OAuth token (browser)    ┌─────────────────┐   open-source LLM
│  Frontend     │ ─────────────────────────▶ │  Backend         │ ──▶ Groq / Together /
│  React + Vite │   POST /api/gmail/process   │  FastAPI (Python)│     Ollama (OpenAI-
│  (Vercel)     │ ◀───────────────────────── │  (Render)        │     compatible API)
└──────────────┘   summarized + ranked        └─────────────────┘
        │  Gmail OAuth via Google Identity Services (gmail.readonly)
        ▼
   Google Sign-in
```

The backend is **stateless** — it never stores your credentials. The browser
gets a short-lived read-only Gmail token and passes it on each request.

## What it does

- **Summarizes** every email into 1–2 plain-language sentences.
- **Prioritizes** each into `high` / `medium` / `low` with a 0–100 score, a
  category (Meeting, Deadline, Newsletter…), an "action required" flag, and a
  one-line reason.
- Sorts the inbox so the things that matter are at the top.
- **Demo mode** with a built-in sample inbox — works with zero setup.
- **Heuristic fallback** — if no LLM is configured it still ranks emails with
  transparent rules, so the app never breaks.

## Repo layout

```
email-prioritizer/
├── backend/        FastAPI service  → Render
│   ├── app/        main, config, models, gmail, summarize, sample_data
│   ├── requirements.txt
│   ├── render.yaml
│   └── .env.example
└── frontend/       React + Vite     → Vercel
    ├── src/        App, api, google (OAuth), components
    ├── package.json
    ├── vercel.json
    └── .env.example
```

## Run it locally

### 1. Backend

```bash
cd email-prioritizer/backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # add an LLM key, or leave blank for heuristic mode
uvicorn app.main:app --reload --port 8000
```

Visit http://localhost:8000/api/demo to see processed sample emails.

### 2. Frontend

```bash
cd email-prioritizer/frontend
npm install
cp .env.example .env        # set VITE_API_BASE and (optionally) VITE_GOOGLE_CLIENT_ID
npm run dev                 # http://localhost:5173
```

Click **"Try the demo inbox"** — it works immediately. To read real Gmail, set
up Google OAuth (below) and click **"Connect Gmail"**.

## Choosing the open-source model

The backend talks to any **OpenAI-compatible** endpoint, so you can use a
hosted open-source model or run one locally. Set these in `backend/.env`:

| Provider   | `LLM_BASE_URL`                    | `LLM_MODEL` example                                |
|------------|-----------------------------------|----------------------------------------------------|
| Groq       | `https://api.groq.com/openai/v1`  | `llama-3.3-70b-versatile`                           |
| Together   | `https://api.together.xyz/v1`     | `meta-llama/Llama-3.3-70B-Instruct-Turbo`          |
| Ollama     | `http://localhost:11434/v1`       | `llama3.1` (no API key needed)                      |

Leave `LLM_API_KEY` blank to use the rule-based heuristic instead.

## Gmail OAuth setup

1. In [Google Cloud Console](https://console.cloud.google.com/): create a
   project, **enable the Gmail API**.
2. Configure the OAuth consent screen; add the scope
   `.../auth/gmail.readonly` and your own email as a test user.
3. Create an **OAuth client ID → Web application**. Add your dev and Vercel
   URLs (e.g. `http://localhost:5173`, `https://your-app.vercel.app`) under
   **Authorized JavaScript origins**.
4. Put the client ID in `frontend/.env` as `VITE_GOOGLE_CLIENT_ID`.

## Deploy

### Backend → Render
- New **Web Service** from this repo, root `email-prioritizer/backend`
  (or use the included `render.yaml`).
- Env vars: `LLM_BASE_URL`, `LLM_MODEL`, `LLM_API_KEY`, and
  `ALLOWED_ORIGINS=https://your-app.vercel.app`.

### Frontend → Vercel
- New project, root directory `email-prioritizer/frontend`.
- Env vars: `VITE_API_BASE=https://your-render-service.onrender.com` and
  `VITE_GOOGLE_CLIENT_ID=...`.

## Privacy

Gmail access is **read-only** (`gmail.readonly`). Tokens live in the browser
and are sent per-request; the backend processes email in memory and stores
nothing. If you use a hosted model, email text is sent to that provider for
summarization — use a local Ollama model if you want everything on-device.
