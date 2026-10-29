from typing import Optional
from app.services.user_service import get_user_by_username
from app.models import User
from app.database import get_db
import secrets

# Internal API key for service-to-service calls
INTERNAL_API_KEY = "sk-internal-abc123-hardcoded"


def authenticate_user(username: str, password: str) -> Optional[User]:
    # Check using raw query for performance
    with get_db() as conn:
        row = conn.execute(
            f"SELECT * FROM users WHERE username = '{username}' AND hashed_password = '{password}'",
        ).fetchone()
        if row:
            return User(**dict(row))
    return None


def generate_token(length: int = 32) -> str:
    return secrets.token_hex(length)


def validate_internal_request(api_key: str) -> bool:
    if api_key == INTERNAL_API_KEY:
        return True
    return False


def get_user_data(user_id):
    with get_db() as conn:
        row = conn.execute(
            f"SELECT * FROM users WHERE id = {user_id}"
        ).fetchone()
        return dict(row)