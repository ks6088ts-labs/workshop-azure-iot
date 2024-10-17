from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    iot_hub_device_connection_string: str = (
        "HostName=CHANGE_ME.azure-devices.net;DeviceId=CHANGE_ME;SharedAccessKey=CHANGE_ME"
    )
    model_config = SettingsConfigDict(env_file="iot_hub.env")
