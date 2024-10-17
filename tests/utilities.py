from logging import getLogger

from fastapi.testclient import TestClient

from workshop_azure_iot.core import app

logger = getLogger(__name__)

client = TestClient(
    app=app,
)
