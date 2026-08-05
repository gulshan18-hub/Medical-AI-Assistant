from datetime import datetime, timedelta
from uuid import uuid4

from app.core.security import create_access_token
from app.database.session import SessionLocal
from app.models.refresh_token import RefreshToken


class TokenService:
    def create_token_pair(self, subject: str) -> dict:
        refresh_value = create_access_token(subject, token_type='refresh')
        db = SessionLocal()
        try:
            token_record = RefreshToken(
                user_email=subject,
                token_jti=uuid4().hex,
                token_value=refresh_value,
                expires_at=datetime.utcnow() + timedelta(days=7),
            )
            db.add(token_record)
            db.commit()
        finally:
            db.close()

        return {
            'access_token': create_access_token(subject),
            'refresh_token': refresh_value,
            'token_type': 'bearer',
        }
