from pydantic_settings import BaseSettings, SettingsConfigDict


class CoreSettings(BaseSettings):
    core_version: str = "0.0.0"
    model_config = SettingsConfigDict(env_file="core.env")
