import base64
from logging import getLogger

from fastapi import APIRouter, UploadFile, status
from fastapi.responses import JSONResponse

from workshop_azure_iot.internals.ai_services import Client
from workshop_azure_iot.settings.ai_services import Settings

logger = getLogger(__name__)

client = Client(
    settings=Settings(),
)

router = APIRouter(
    prefix="/ai_services",
    tags=["ai_services"],
)


@router.post("/chat/completions")
async def chat_completions(prompt: str):
    response = await client.chat_completions(
        [
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response,
    )


@router.post("/chat/completions_with_image")
async def chat_completions_with_image(
    file: UploadFile,
    prompt: str,
):
    image = await file.read()
    encoded_image = base64.b64encode(image).decode()
    response = await client.chat_completions(
        [
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"},
                    },
                    {
                        "type": "text",
                        "text": prompt,
                    },
                ],
            },
        ]
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response,
    )
