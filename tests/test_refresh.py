import sys
import uuid
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))

from app.main import app

client = TestClient(app)


def test_refresh_token_flow():
    test_email = f"{uuid.uuid4().hex}@example.com"
    signup_response = client.post(
        '/api/v1/auth/signup',
        json={
            'email': test_email,
            'full_name': 'Refresh User',
            'password': 'StrongPass123!',
        },
    )
    assert signup_response.status_code == 201
    payload = signup_response.json()
    assert payload['role'] == 'user'

    refresh_response = client.post(
        '/api/v1/auth/refresh',
        json={'refresh_token': payload['refresh_token']},
    )
    assert refresh_response.status_code == 200
    refreshed_payload = refresh_response.json()
    assert refreshed_payload['email'] == test_email
    assert refreshed_payload['role'] == 'user'
    assert 'access_token' in refreshed_payload
    assert 'refresh_token' in refreshed_payload
