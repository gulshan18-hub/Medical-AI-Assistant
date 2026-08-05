from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.database.base import Base
from app.database.session import engine
from app.models.refresh_token import RefreshToken  # noqa: F401
from app.models.user import User  # noqa: F401

app = FastAPI(title="Medical AI Assistant Pro", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "medical-ai-assistant-pro"}
