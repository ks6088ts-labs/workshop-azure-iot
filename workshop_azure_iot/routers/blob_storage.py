from logging import getLogger

from fastapi import APIRouter, UploadFile, status
from fastapi.responses import JSONResponse, Response

from workshop_azure_iot.internals.blob_storage import Client
from workshop_azure_iot.settings.blob_storage import Settings

logger = getLogger(__name__)

client = Client(
    settings=Settings(),
)

router = APIRouter(
    prefix="/blob_storage",
    tags=["blob_storage"],
)


@router.get(
    "/images/{blob_name}",
    responses={200: {"content": {"image/jpeg": {}}}},
    response_class=Response,
)
async def get_image(
    blob_name: str,
):
    image_bytes = client.download_blob_stream(
        blob_name=blob_name,
    )
    return Response(
        content=image_bytes,
        media_type="image/jpeg",
    )


@router.get(
    "/images",
)
async def list_images():
    return client.list_blobs()


@router.post(
    "/images",
    status_code=201,
)
async def upload_image(
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
