from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="app/.env", extra="ignore")
    APP_VERSION: str = "v1"
    API_BASE_URL: str = "/api"


MyAppConfig = AppConfig()
