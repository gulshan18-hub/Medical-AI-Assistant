from sqlalchemy.orm import Session

from app.models.user import User
from app.services.password import get_password_hash
from app.services.token import TokenService


class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.token_service = TokenService()

    def signup(self, email: str, full_name: str, password: str):
        user = User(
            email=email,
            full_name=full_name,
            hashed_password=get_password_hash(password),
            role='user',
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        tokens = self.token_service.create_token_pair(email)
        return {
            **tokens,
            'email': user.email,
            'full_name': user.full_name,
            'role': user.role,
        }

    def login(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            raise ValueError('Invalid email or password')
        if not self._verify_password(user, password):
            raise ValueError('Invalid email or password')
        tokens = self.token_service.create_token_pair(email)
        return {
            **tokens,
            'email': user.email,
            'full_name': user.full_name,
            'role': user.role,
        }

    def _verify_password(self, user: User, password: str) -> bool:
        from app.services.password import verify_password

        return verify_password(password, user.hashed_password)
