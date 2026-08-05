import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))

from app.llm.provider import LLMProvider, ProviderRouter


def test_provider_router_builds_prompt():
    router = ProviderRouter(provider=LLMProvider.GEMINI)
    prompt = router.build_system_prompt()
    assert 'medical education assistant' in prompt.lower()
    assert 'educational-only notice' in prompt.lower()
