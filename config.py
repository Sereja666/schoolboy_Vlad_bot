from pathlib import Path
from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")





class Settings(BaseSettings):
    TOKEN: str = os.environ.get("TOKEN")
    db_url: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


settings = Settings()
