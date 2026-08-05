from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import ALGORITHM, SECRET_KEY
from app.database.session import SessionLocal, get_db
from app.models.refresh_token import RefreshToken
from app.schemas.auth import AuthResponse, LoginRequest, SignupRequest
from app.schemas.refresh import RefreshTokenRequest, RefreshTokenResponse
from app.services.refresh import RefreshTokenService
from app.services.user import UserService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
def signup(payload: SignupRequest, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        return service.signup(payload.email, payload.full_name, payload.password)
    except IntegrityError as exc:
        raise HTTPException(status_code=409, detail="A user with this email already exists.") from exc
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        return service.login(payload.email, payload.password)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc


@router.post("/refresh", response_model=RefreshTokenResponse)
def refresh(payload: RefreshTokenRequest):
    try:
        decoded = jwt.decode(payload.refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception as exc:
        raise HTTPException(status_code=401, detail="Invalid refresh token") from exc

    if decoded.get('token_type') != 'refresh':
        raise HTTPException(status_code=401, detail='Invalid refresh token type')

    db = SessionLocal()
    try:
        token_record = db.query(RefreshToken).filter(RefreshToken.token_value == payload.refresh_token).first()
        if not token_record or token_record.is_revoked:
            raise HTTPException(status_code=401, detail='Refresh token is invalid or revoked')
    finally:
        db.close()

    service = RefreshTokenService()
    return service.refresh(decoded['sub'], previous_token=payload.refresh_token)
