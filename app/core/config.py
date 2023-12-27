from typing import Optional
from pathlib import Path

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    app_description: str = 'Кошачий благотворительный фонд'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    jwt_token_lifetime: int = 3600
    user_password_min_len: int = 3
    logging_format: str = '%(asctime)s - %(levelname)s - %(message)s'
    logging_dt_format: str = '%Y-%m-%d %H:%M:%S'
    # Переменные для GoogleAPI
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    class Config:
        env_file = f'{Path(__file__).resolve().parent}/.env'


settings = Settings()
