import azure.functions as func
from dotenv import load_dotenv

from workshop_azure_iot.core import app as fastapi_app

load_dotenv()

app = func.AsgiFunctionApp(
    app=fastapi_app,
    http_auth_level=func.AuthLevel.ANONYMOUS,
)
