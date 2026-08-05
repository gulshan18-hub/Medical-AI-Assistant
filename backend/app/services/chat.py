class ChatService:
    """Medical-safe chatbot orchestration placeholder with provider-ready design."""

    EMERGENCY_KEYWORDS = {
        'chest pain',
        'difficulty breathing',
        'stroke symptoms',
        'severe bleeding',
        'unconsciousness',
    }

    def __init__(self) -> None:
        self.system_notice = (
            "This information is for educational purposes only. "
            "It does not replace a licensed medical professional."
        )

    def detect_emergency(self, user_message: str) -> bool:
        text = user_message.lower()
        return any(keyword in text for keyword in self.EMERGENCY_KEYWORDS)

    def generate_safe_reply(self, user_message: str) -> dict:
        emergency_notice = None
        if self.detect_emergency(user_message):
            emergency_notice = (
                "Emergency warning: seek immediate emergency medical care right away. "
                "If you are experiencing a medical emergency, call emergency services now."
            )

        return {
            'reply': (
                f"{self.system_notice}\n\n"
                f"You asked: {user_message}\n"
                "A production LLM workflow will connect here with provider switching, "
                "guardrails, and source citations."
            ),
            'educational_notice': self.system_notice,
            'emergency_notice': emergency_notice,
        }
