from pydantic_settings import BaseSettings, SettingsConfigDict


class CoreSettings(BaseSettings):
    core_version: str
    model_config = SettingsConfigDict(env_file="core.env")
