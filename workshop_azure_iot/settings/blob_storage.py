from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    blob_storage_account_name: str
    blob_storage_container_name: str
    blob_storage_sas_token: str

    model_config = SettingsConfigDict(env_file="blob_storage.env")
