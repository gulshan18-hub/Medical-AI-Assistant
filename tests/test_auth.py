import sys
import uuid
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))

from app.main import app

client = TestClient(app)


def test_signup_and_login_flow():
    test_email = f"{uuid.uuid4().hex}@example.com"
    signup_response = client.post(
        '/api/v1/auth/signup',
        json={
            'email': test_email,
            'full_name': 'Test User',
            'password': 'StrongPass123!',
        },
    )
    assert signup_response.status_code == 201
    signup_payload = signup_response.json()
    assert signup_payload['email'] == test_email
    assert 'access_token' in signup_payload
    assert 'refresh_token' in signup_payload

    login_response = client.post(
        '/api/v1/auth/login',
        json={
            'email': test_email,
            'password': 'StrongPass123!',
        },
    )
    assert login_response.status_code == 200
    login_payload = login_response.json()
    assert login_payload['email'] == test_email
    assert 'access_token' in login_payload
    assert 'refresh_token' in login_payload
