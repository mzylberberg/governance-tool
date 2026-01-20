# Governance Translator

A portfolio project that translates technical cybersecurity/IT language into stakeholder-ready communication (IT, Executives, Project/Program teams), with structured outputs for risk, impact, and next actions.

- 📄 [Product Requirements Document (PRD)](docs/PRD.md)
## Features (MVP)
- Translate technical text into audience-specific language (IT / Executive / PM)
- Structured output: summary, key risks, business impact, recommended actions
- Save translation history to SQLite (backend)
- Clean React UI with FastAPI API backend

## Tech Stack
- Frontend: React (Vite)
- Backend: FastAPI (Python)
- Database: SQLite

## Monorepo Structure
```
governance-tool/
  frontend/
  backend/
  docs/
  README.md
```


## Getting Started (Local)
### Backend
1. Create venv (Python 3.13)
2. Install dependencies
3. Run FastAPI server

### Frontend
1. Install dependencies
2. Run dev server
3. Open the app in browser

## API (planned)
- GET /health
- POST /translate
- GET /history

## Roadmap
- Add basic tests (pytest)
- Add linting/formatting (ruff)
- Deploy frontend (Vercel) + backend (Render/Fly) for a live demo
- Add authentication (optional)

## Screenshots
(coming soon)
