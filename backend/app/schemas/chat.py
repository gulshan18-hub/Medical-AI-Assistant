from pydantic import BaseModel


class ChatMessageRequest(BaseModel):
    message: str


class ChatMessageResponse(BaseModel):
    reply: str
    educational_notice: str
    emergency_notice: str | None = None
