from enum import Enum

from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import CloudToDeviceMethod, CloudToDeviceMethodResult

from workshop_azure_iot.settings.iot_hub import Settings
from workshop_azure_iot.utilities import get_logger

logger = get_logger(name=__name__)


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
        logger.info("Connecting to IoT Hub")
        await self.device_client.connect()
        self.state = State.CONNECTED

    async def shutdown(self):
        if self.state == State.DISCONNECTED:
            return
        logger.info("Shutting down IoT Hub connection")
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

    async def call_direct_method(self, method_name: str, payload: dict):
        # https://learn.microsoft.com/ja-jp/azure/iot-hub/device-management-python#create-a-device-app-with-a-direct-method
        try:
            registry_manager = IoTHubRegistryManager(connection_string=self.settings.iot_hub_connection_string)
            deviceMethod = CloudToDeviceMethod(method_name=method_name, payload=payload)
            response: CloudToDeviceMethodResult = registry_manager.invoke_device_method(
                device_id=self.settings.iot_hub_device_id,
                direct_method_request=deviceMethod,
            )
        except Exception as e:
            logger.error(f"Failed to connect to IoT Hub: {e}")
            return {"error": f"Failed to connect to IoT Hub: {e}"}
        return response.as_dict()
