from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    app_name:str = "TaskFlow"
    environment:str = "development"

    database_url:str = (
        f"sqlite:///{(BACKEND_DIR / "taskflow.db").as_posix()}"
    )

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()