from fastapi import APIRouter, UploadFile, status
from fastapi.responses import JSONResponse, Response

from workshop_azure_iot.internals.blob_storage import Client
from workshop_azure_iot.settings.blob_storage import Settings
from workshop_azure_iot.utilities import get_logger

logger = get_logger(name=__name__)

client = Client(
    settings=Settings(),
)

router = APIRouter(
    prefix="/blob_storage",
    tags=["blob_storage"],
)


@router.get(
    "/{blob_name}",
    response_class=Response,
)
async def get_blob(
    blob_name: str,
):
    return Response(
        content=client.download_blob_stream(
            blob_name=blob_name,
        ),
    )


@router.get(
    "/",
)
async def list_blobs():
    return client.list_blobs()


@router.post(
    "/",
    status_code=201,
)
async def upload_blob(
    file: UploadFile,
    blob_name: str,
):
    content = await file.read()
    response = client.upload_blob_stream(
        blob_name=blob_name,
        stream=content,
    )
    logger.warning(f"Response: {response}, type: {type(response)}")
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": "Image uploaded successfully",
            "etag": response.get("etag"),
        },
    )


@router.get(
    "/images/{device_name}/{file_name}",
    responses={200: {"content": {"image/jpeg": {}}}},
    response_class=Response,
)
async def get_image(
    device_name: str,
    file_name: str,
):
    image_bytes = client.download_blob_stream(
        blob_name=f"{device_name}/{file_name}",
    )
    return Response(
        content=image_bytes,
        media_type="image/jpeg",
    )
