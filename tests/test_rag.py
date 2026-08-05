import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))

from app.main import app

client = TestClient(app)


def test_document_upload_and_rag_question():
    upload_response = client.post(
        '/api/v1/documents/upload',
        files={'file': ('sample.txt', b'Cancer screening guidelines recommend early awareness. Symptoms include fatigue and weight changes.')},
    )
    assert upload_response.status_code == 201
    upload_payload = upload_response.json()
    assert upload_payload['source'] == 'sample.txt'

    ask_response = client.post(
        '/api/v1/documents/ask',
        json={'question': 'What does cancer screening recommend?'}
    )
    assert ask_response.status_code == 200
    ask_payload = ask_response.json()
    assert 'Cancer screening guidelines recommend early awareness.' in ask_payload['answer']
    assert ask_payload['sources'][0]['source'] == 'sample.txt'
