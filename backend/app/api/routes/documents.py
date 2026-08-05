from fastapi import APIRouter, Body, File, HTTPException, UploadFile
from pydantic import BaseModel

from app.services.rag import RAGService

router = APIRouter(prefix="/documents", tags=["documents"])
rag_service = RAGService()


class AskQuestionRequest(BaseModel):
    question: str


@router.post("/upload", status_code=201)
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="A file is required")
    content = await file.read()
    text = content.decode('utf-8', errors='ignore')
    return rag_service.index_text(text, file.filename)


@router.post("/ask")
def ask_document_question(payload: AskQuestionRequest = Body(...)):
    return rag_service.answer_question(payload.question)
