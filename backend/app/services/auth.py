class AuthService:
    """Authentication service placeholder for JWT and password hashing workflows."""

    def authenticate(self, email: str, password: str) -> bool:
        return bool(email and password)
