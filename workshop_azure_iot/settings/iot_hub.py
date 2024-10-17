from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    iot_hub_device_connection_string: str
    model_config = SettingsConfigDict(env_file="iot_hub.env")
