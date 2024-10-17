from logging import getLogger

from azure.iot.device.aio import IoTHubDeviceClient

from workshop_azure_iot.settings.iot_hub import Settings

logger = getLogger(__name__)


class Client:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def get_device_twin(self) -> dict:
        client = IoTHubDeviceClient.create_from_connection_string(self.settings.iot_hub_device_connection_string)
        # FIXME: to make it faster, connection should be established once and reused
        await client.connect()
        twin = await client.get_twin()
        await client.shutdown()
        return twin
