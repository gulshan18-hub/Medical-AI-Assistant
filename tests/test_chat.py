import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))

from app.main import app

client = TestClient(app)


def test_chat_message_returns_safety_notice():
    response = client.post(
        '/api/v1/chat/message',
        json={'message': 'I have a mild headache and feel tired.'},
    )
    assert response.status_code == 200
    payload = response.json()
    assert 'This information is for educational purposes only.' in payload['educational_notice']
    assert 'headache' in payload['reply']
