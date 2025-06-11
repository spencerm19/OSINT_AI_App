from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, PostgresDsn, validator
import os

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    ALGORITHM: str = "HS256"

    # CORS configuration
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Database configuration
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://osint:osint@localhost:5432/osint"
    )
    REDIS_URL: str = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379/0"
    )
    NEO4J_URI: str = os.getenv(
        "NEO4J_URI",
        "bolt://localhost:7687"
    )
    NEO4J_USER: str = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "osintbuddy")

    # Redis configuration
    REDIS_HOST: str
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Optional[str] = None

    # Email configuration
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    # AI configuration
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    DEFAULT_AI_MODEL: str = "gpt-4"

    # n8n configuration
    N8N_URL: Optional[str] = None
    N8N_API_KEY: Optional[str] = None

    # Application configuration
    PROJECT_NAME: str = "OSINT Buddy"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "Modern OSINT Research Platform"
    DEBUG: bool = False
    SQLALCHEMY_ECHO: bool = False

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 