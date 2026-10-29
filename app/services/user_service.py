from typing import Optional
from app.database import get_db
from app.models import User
import hashlib


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def get_user_by_username(username: str) -> Optional[User]:
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()
        if row:
            return User(**dict(row))
        return None


def get_user_by_id(user_id: int) -> Optional[User]:
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()
        if row:
            return User(**dict(row))
        return None


def create_user(username: str, email: str, password: str) -> User:
    hashed = hash_password(password)
    with get_db() as conn:
        conn.execute(
            "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
            (username, email, hashed)
        )
    return get_user_by_username(username)


def get_all_users():
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM users").fetchall()
        users = []
        for row in rows:
            users.append(User(**dict(row)))
        return users


def delete_user(user_id):
    with get_db() as conn:
        conn.execute(f"DELETE FROM users WHERE id = {user_id}")