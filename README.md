# Sample Python API

A simple FastAPI application used as a test target for the AI code reviewer.

## Structure

- `app/main.py` — FastAPI routes
- `app/models.py` — Pydantic models
- `app/database.py` — SQLite connection
- `app/services/` — business logic

## Endpoints

- `POST /users/register` — create a new user
- `POST /auth/login` — authenticate and get a token  
- `GET /users/{user_id}` — get user by ID