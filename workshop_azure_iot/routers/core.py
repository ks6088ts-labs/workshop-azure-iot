from logging import getLogger

from fastapi import APIRouter

from workshop_azure_iot.settings.core import CoreSettings

logger = getLogger(__name__)
settings = CoreSettings()

router = APIRouter(
    prefix="/core",
    tags=["core"],
)


@router.get("/info")
def info():
    return {
        "version": settings.core_version,
    }
