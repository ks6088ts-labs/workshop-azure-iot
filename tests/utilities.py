from logging import getLogger
from os import getenv

from fastapi.testclient import TestClient

from workshop_azure_iot.core import app

logger = getLogger(__name__)

client = TestClient(
    app=app,
)

SKIP_TEST = getenv("SKIP_TEST", "False") == "True"
