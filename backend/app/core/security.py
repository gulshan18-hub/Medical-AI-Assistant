from datetime import datetime, timedelta, timezone

from jose import jwt

SECRET_KEY = "change-me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7


def create_access_token(subject: str, token_type: str = "access") -> str:
    if token_type == "refresh":
        expires_delta = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    else:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {
        "sub": subject,
        "exp": datetime.now(timezone.utc) + expires_delta,
        "token_type": token_type,
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
