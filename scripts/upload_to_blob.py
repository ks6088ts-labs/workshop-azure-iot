import asyncio
import logging
from os import getenv

import typer
from azure.core.exceptions import ResourceExistsError
from azure.iot.device.aio import IoTHubDeviceClient
from azure.storage.blob import BlobClient
from dotenv import load_dotenv

app = typer.Typer()
logger = logging.getLogger(__name__)


async def upload_to_blob(
    device_client: IoTHubDeviceClient,
    data: bytes,
    blob_name: str,
):
    # get the Storage SAS information from IoT Hub.
    storage_info = await device_client.get_storage_info_for_blob(blob_name)
    logger.info(f"Got Storage Info: {storage_info}")
    result = {
        "status_code": -1,
        "status_description": "N/A",
    }

    # Using the Storage Blob V12 API, perform the blob upload.
    try:
        blob_client = BlobClient.from_blob_url(
            blob_url=f"https://{storage_info['hostName']}/{storage_info['containerName']}/{storage_info['blobName']}{storage_info['sasToken']}"
        )

        upload_result = blob_client.upload_blob(
            data=data,
            overwrite=True,
        )

        if hasattr(upload_result, "error_code"):
            result = {
                "status_code": upload_result.error_code,
                "status_description": "Storage Blob Upload Error",
            }
        else:
            result = {
                "status_code": 200,
                "status_description": "",
            }
    except ResourceExistsError as ex:
        if ex.status_code:
            result = {
                "status_code": ex.status_code,
                "status_description": ex.reason,
            }
        else:
            logger.error("Failed with Exception: {}", ex)
            result = {
                "status_code": 400,
                "status_description": ex.message,
            }

    logger.info(f"Upload Result: {result}")

    if result["status_code"] == 200:
        await device_client.notify_blob_upload_status(
            storage_info["correlationId"], True, result["status_code"], result["status_description"]
        )
    else:
        await device_client.notify_blob_upload_status(
            storage_info["correlationId"],
            False,
            result["status_code"],
            result["status_description"],
        )
    return result


async def main_impl(
    data: bytes,
    blob_name: str,
):
    device_client = IoTHubDeviceClient.create_from_connection_string(getenv("IOT_HUB_DEVICE_CONNECTION_STRING"))

    # connect the client.
    await device_client.connect()
    logger.info("Connected with Azure IoT Hub")

    await upload_to_blob(
        device_client=device_client,
        data=data,
        blob_name=blob_name,
    )

    # Finally, shut down the client
    await device_client.shutdown()


@app.command()
def main(
    file_path: str = typer.Option("README.md", help="Path to the file to upload."),
    blob_name: str = typer.Option("test", help="Name of the blob to upload."),
    verbose: bool = False,
):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    with open(file_path, "rb") as f:
        data = f.read()

    asyncio.run(
        main_impl(
            data=data,
            blob_name=blob_name,
        )
    )


if __name__ == "__main__":
    load_dotenv("iot_hub.env")
    app()
