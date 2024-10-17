from fastapi import FastAPI

from workshop_azure_iot.routers.core import router as core_router
from workshop_azure_iot.routers.iot_hub import router as iot_hub_router

app = FastAPI(
    docs_url="/",
)

for router in [
    core_router,
    iot_hub_router,
    # Add routers here
]:
    app.include_router(router)
