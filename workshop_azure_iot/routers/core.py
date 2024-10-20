from fastapi import APIRouter

from workshop_azure_iot.settings.core import CoreSettings
from workshop_azure_iot.utilities import get_logger

settings = CoreSettings()
logger = get_logger(name=__name__)

router = APIRouter(
    prefix="/core",
    tags=["core"],
)


@router.get("/info")
def info():
    return {
        "version": settings.core_version,
    }
