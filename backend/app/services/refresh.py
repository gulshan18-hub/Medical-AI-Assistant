from datetime import datetime, timedelta
from uuid import uuid4

from app.core.security import create_access_token
from app.database.session import SessionLocal
from app.models.refresh_token import RefreshToken
from app.models.user import User


class RefreshTokenService:
    def refresh(self, subject: str, previous_token: str | None = None) -> dict:
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.email == subject).first()
            if not user:
                raise ValueError('User not found')

            if previous_token:
                revoked_record = db.query(RefreshToken).filter(RefreshToken.token_value == previous_token).first()
                if revoked_record:
                    revoked_record.is_revoked = True

            refresh_value = create_access_token(subject, token_type='refresh')
            token_record = RefreshToken(
                user_email=subject,
                token_jti=uuid4().hex,
                token_value=refresh_value,
                expires_at=datetime.utcnow() + timedelta(days=7),
            )
            db.add(token_record)
            db.commit()

            return {
                'access_token': create_access_token(subject),
                'refresh_token': refresh_value,
                'token_type': 'bearer',
                'email': subject,
                'role': user.role,
                'full_name': user.full_name,
            }
        finally:
            db.close()
