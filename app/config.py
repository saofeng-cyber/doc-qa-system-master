from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="app/.env", extra="ignore")
    APP_VERSION: str = "v1"
    API_BASE_URL: str = "/api"
    DATABASE_URL: str = "sqlite:///database.db"
    DATABASE_ECHO: bool = False
    DATABASE_NAME: str = "saofeng"


MyAppConfig = AppConfig()
