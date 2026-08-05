# Medical AI Assistant Pro

A professional, healthcare-safe AI assistant platform built as a modular monorepo with a FastAPI backend, React frontend, and a security-first product posture.

## Product overview

Medical AI Assistant Pro is an educational medical AI platform intended to help users understand:
- symptoms and triage concepts
- disease definitions and risk factors
- medicine information
- uploaded medical documents
- health summaries and recommended next steps

The assistant does not replace a licensed medical professional and includes explicit educational-use notices.

## Safety-first principles

- never claims to be a doctor
- always provides an educational-only notice
- detects emergency phrases and advises urgent care
- blocks unsafe/out-of-scope medical advice
- supports source-grounded retrieval for document workflows

## Tech stack

- Backend: FastAPI, Python, SQLAlchemy, Pydantic
- Frontend: React, TypeScript, Tailwind CSS, Framer Motion
- Storage: SQLite for current lightweight local persistence, ready for PostgreSQL migration
- AI: provider-ready LLM abstraction with RAG-first retrieval layer
- DevOps: Docker, GitHub Actions, pytest, Vite build validation

## Repository structure

- backend/ — API app, services, models, schemas, routers
- frontend/ — React landing application and design system shell
- docs/ — architecture, roadmap, and product guidance
- docker/ — containerization artifacts
- tests/ — regression and integration coverage
- scripts/ — operational automation

## Local run

Backend:

```powershell
cd backend
python -m uvicorn app.main:app --reload
```

Frontend:

```powershell
cd frontend
npm install
npm run dev
```

## Verified current status

The project currently includes a validated scaffold for:
- health API
- auth signup/login flow
- document upload and question retrieval
- chat safety reply model
- frontend landing experience

## Next roadmap

- provider switching for Gemini/OpenAI
- PostgreSQL migration
- robust JWT refresh token architecture
- medical report ingestion and OCR
- analytics, dashboards, and admin features
