from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


MONGO_DB_URI = "mongodb://localhost:27017/minimed"


class Settings(BaseSettings):
    """Configuration data model

    Attributes:
        auth_token_expire_minutes (int): The auth token expiration time
        mongo_db_uri (str): The DB URI
        log_level (str): The log level
        secret_key: (str) = The secret key
    """

    auth_token_expire_minutes: int = Field(
        alias="AUTH_TOKEN_EXPIRE_MINUTES",
        default=1440,
    )
    mongo_db_uri: str = Field(
        alias="DB_URI",
        default=MONGO_DB_URI,
    )
    log_level: str = Field(
        alias="LOG_LEVEL",
        default="INFO",
    )
    secret_key: str = Field(
        alias="SECRET_KEY",
        default="",
    )
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
