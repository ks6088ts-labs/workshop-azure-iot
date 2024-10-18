from enum import Enum
from logging import getLogger

from azure.iot.device.aio import IoTHubDeviceClient

from workshop_azure_iot.settings.iot_hub import Settings

logger = getLogger(__name__)


class State(Enum):
    DISCONNECTED = "disconnected"
    CONNECTED = "connected"


class Client:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.device_client = IoTHubDeviceClient.create_from_connection_string(
            self.settings.iot_hub_device_connection_string
        )
        self.state = State.DISCONNECTED

    async def connect(self):
        if self.state == State.CONNECTED:
            return
        await self.device_client.connect()
        self.state = State.CONNECTED

    async def shutdown(self):
        if self.state == State.DISCONNECTED:
            return
        await self.device_client.shutdown()
        self.state = State.DISCONNECTED

    async def get_device_twin(self) -> dict:
        # https://learn.microsoft.com/azure/iot-hub/how-to-device-twins?pivots=programming-language-python#retrieve-a-device-twin-and-examine-reported-properties
        await self.connect()
        return await self.device_client.get_twin()

    async def patch_device_twin(self, reported_properties: dict):
        # https://learn.microsoft.com/azure/iot-hub/how-to-device-twins?pivots=programming-language-python#patch-reported-device-twin-properties
        await self.connect()
        await self.device_client.patch_twin_reported_properties(reported_properties_patch=reported_properties)
