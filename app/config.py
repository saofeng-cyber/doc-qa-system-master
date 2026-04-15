from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="app/.env", extra="ignore")
    APP_VERSION: str = "v1"
    API_BASE_URL: str = "/api"
    AVAILABLE_MODELS: str = Field(
        default="deepseek-chat", description="模型名称, 默认为deepseek-chat"
    )
    BASE_URL: str = ""
    API_KEY: str = ""
    MODEL_PROVIDER: str = Field(
        default="openai", description="模型供应商，默认为openai"
    )


MyAppConfig = AppConfig()
