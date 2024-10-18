from fastapi import FastAPI

from workshop_azure_iot.routers.ai_services import router as ai_services_router
from workshop_azure_iot.routers.blob_storage import router as blob_storage_router
from workshop_azure_iot.routers.core import router as core_router
from workshop_azure_iot.routers.iot_hub import router as iot_hub_router

app = FastAPI(
    docs_url="/",
)

for router in [
    core_router,
    iot_hub_router,
    ai_services_router,
    blob_storage_router,
    # Add routers here
]:
    app.include_router(router)
