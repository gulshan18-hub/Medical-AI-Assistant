from enum import Enum


class LLMProvider(str, Enum):
    OPENAI = "openai"
    GEMINI = "gemini"


class ProviderRouter:
    """Lightweight provider abstraction for future switching between LLM backends."""

    def __init__(self, provider: LLMProvider = LLMProvider.GEMINI) -> None:
        self.provider = provider

    def build_system_prompt(self) -> str:
        return (
            "You are a medical education assistant. "
            "Always include the educational-only notice. "
            "Never claim to be a doctor."
        )
