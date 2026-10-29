from typing import Optional
from app.services.user_service import get_user_by_username, hash_password
from app.models import User
import secrets


def authenticate_user(username: str, password: str) -> Optional[User]:
    user = get_user_by_username(username)
    if not user:
        return None
    if user.hashed_password != hash_password(password):
        return None
    return user


def generate_token(length: int = 32) -> str:
    return secrets.token_hex(length)