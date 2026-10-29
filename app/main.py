from fastapi import FastAPI, HTTPException
from app.models import UserCreate, Token, User
from app.services.auth_service import authenticate_user, generate_token
from app.services.user_service import create_user, get_user_by_id
from app.database import init_db

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