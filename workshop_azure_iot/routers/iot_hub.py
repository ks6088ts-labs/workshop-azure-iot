from logging import getLogger

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from workshop_azure_iot.internals.iot_hub import Client
from workshop_azure_iot.settings.iot_hub import Settings

logger = getLogger(__name__)

client = Client(
    settings=Settings(),
)

router = APIRouter(
    prefix="/iot_hub",
    tags=["iot_hub"],
)


@router.get("/device_twin")
async def get_device_twin():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await client.get_device_twin(),
    )


@router.patch("/device_twin")
async def patch_device_twin(reported_properties: dict):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await client.patch_device_twin(reported_properties),
    )


@router.post("/call_direct_method")
async def call_direct_method(
    method_name: str,
    payload: dict,
):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await client.call_direct_method(
            method_name=method_name,
            payload=payload,
        ),
    )
