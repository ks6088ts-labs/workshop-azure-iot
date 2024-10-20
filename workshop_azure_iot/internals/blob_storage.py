from azure.storage.blob import BlobServiceClient

from workshop_azure_iot.settings.blob_storage import Settings
from workshop_azure_iot.utilities import get_logger

logger = get_logger(name=__name__)


class Client:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.blob_service_client = BlobServiceClient(
            account_url=f"https://{self.settings.blob_storage_account_name}.blob.core.windows.net",
            credential=self.settings.blob_storage_sas_token,
        )

    def download_blob_stream(
        self,
        blob_name: str,
    ) -> bytes:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.settings.blob_storage_container_name,
            blob=blob_name,
        )
        logger.info(f"Downloaded blob {blob_name} from container {self.settings.blob_storage_container_name}")
        return blob_client.download_blob().readall()

    def upload_blob_stream(
        self,
        blob_name: str,
        stream: bytes,
    ) -> dict:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.settings.blob_storage_container_name,
            blob=blob_name,
        )
        logger.info(f"Uploaded blob {blob_name} to container {self.settings.blob_storage_container_name}")
        return blob_client.upload_blob(stream, overwrite=True)

    def list_blobs(
        self,
    ) -> list:
        container_client = self.blob_service_client.get_container_client(self.settings.blob_storage_container_name)
        logger.info(f"Listed blobs in container {self.settings.blob_storage_container_name}")
        return [blob.name for blob in container_client.list_blobs()]
