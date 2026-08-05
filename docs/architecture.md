# Medical AI Assistant Pro Architecture

## Goal

The application follows a modular monorepo architecture designed for a healthcare AI SaaS product. It separates frontend, backend, data, LLM orchestration, and safety control surfaces so it can evolve into a production-grade system.

## Layered design

- API Layer: FastAPI routers, request validation, dependency injection
- Service Layer: authentication, document retrieval, medical chat, user workflows
- Data Layer: SQLAlchemy models and lightweight persistence
- Retrieval Layer: source-aware document ingestion and question answering
- Safety Layer: educational disclaimer, emergency detection, content guardrails
- DevOps Layer: Docker, CI, test automation, environment management

## Product posture

The platform is designed for educational health assistance workflows, not diagnosis replacement. All LLM-facing responses are intended to stay within clear, clinician-safe boundaries.

## Production hardening roadmap

- PostgreSQL migration
- JWT refresh token rotation
- provider abstraction for Gemini/OpenAI
- cache and embedding persistence
- metrics, tracing, and prompt versioning
- admin analytics and billing visibility
