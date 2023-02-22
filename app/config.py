"""App module."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings class."""
    DB_HOST: str
    DB_HOSTNAME: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    USER_SECRET: str
    ALGORITHM: str
    CURRENCIES: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM: str

    class Config:
        """Config class."""
        env_file = './.env'


settings = Settings()
