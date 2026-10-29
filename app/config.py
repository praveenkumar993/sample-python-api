import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "sample-python-api"
    database_url: str = "sqlite:///./app.db"
    secret_key: str = os.getenv("SECRET_KEY", "changeme")
    debug: bool = False


settings = Settings()