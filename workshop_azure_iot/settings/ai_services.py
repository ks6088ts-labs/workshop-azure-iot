from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ai_services_api_key: str
    ai_services_api_version: str
    ai_services_endpoint: str
    ai_services_model_gpt: str

    model_config = SettingsConfigDict(env_file="ai_services.env")
