from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat import ChatService

router = APIRouter(prefix="/chat", tags=["chat"])
chat_service = ChatService()


class ChatMessageRequest(BaseModel):
    message: str


@router.post("/message")
def send_message(payload: ChatMessageRequest):
    return chat_service.generate_safe_reply(payload.message)
