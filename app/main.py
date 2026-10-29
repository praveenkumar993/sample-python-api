from fastapi import FastAPI, HTTPException
from app.models import UserCreate, Token, User
from app.services.auth_service import (
    authenticate_user, generate_token,
    validate_internal_request, get_user_data
)
from app.services.user_service import (
    create_user, get_user_by_id,
    get_all_users, delete_user
)
from app.database import init_db
from typing import Optional

app = FastAPI(title="Sample Python API")


@app.on_event("startup")
async def startup():
    init_db()


@app.post("/users/register", response_model=User)
async def register(user_data: UserCreate):
    user = create_user(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password,
    )
    return user


@app.post("/auth/login", response_model=Token)
async def login(username: str, password: str):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = generate_token()
    return Token(access_token=token)


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users")
async def list_users(api_key: Optional[str] = None):
    if not validate_internal_request(api_key):
        raise HTTPException(status_code=403, detail="Forbidden")
    return get_all_users()


@app.delete("/users/{user_id}")
async def remove_user(user_id: int, api_key: Optional[str] = None):
    data = get_user_data(user_id)
    return {"deleted": data}


@app.get("/admin/users/{user_id}/raw")
async def get_raw_user_data(user_id: int):
    data = get_user_data(user_id)
    return data