from fastapi import FastAPI

from workshop_azure_iot.routers.core import router as core_router

app = FastAPI(
    docs_url="/",
)

for router in [
    core_router,
    # Add routers here
]:
    app.include_router(router)
