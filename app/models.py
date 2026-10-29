from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    hashed_password: str
    is_active: bool = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"