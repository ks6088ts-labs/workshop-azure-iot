import asyncio
import logging
from os import getenv

import typer
from azure.iot.device import MethodResponse
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device.iothub.models.methods import MethodRequest
from dotenv import load_dotenv

app = typer.Typer()
logger = logging.getLogger(__name__)


async def receive_direct_method_impl():
    # https://github.com/Azure/azure-iot-sdk-python/blob/main/samples/async-hub-scenarios/receive_direct_method.py
    device_client = IoTHubDeviceClient.create_from_connection_string(getenv("IOT_HUB_DEVICE_CONNECTION_STRING"))

    # connect the client.
    await device_client.connect()

    # Define behavior for handling methods
    async def method_request_handler(method_request: MethodRequest):
        logger.info(method_request.name)
        logger.info(method_request.payload)

        # TODO: Determine how to respond to the method request based on the method name

        # Send the response
        method_response = MethodResponse.create_from_method_request(
            method_request=method_request,
            status=200,
            payload={
                "result": "Successfully executed method",
                "request": {
                    "name": method_request.name,
                    "payload": method_request.payload,
                },
            },
        )
        await device_client.send_method_response(method_response)

    # Set the method request handler on the client
    device_client.on_method_request_received = method_request_handler

    # Define behavior for halting the application
    def stdin_listener():
        while True:
            selection = input("Press Q to quit\n")
            if selection == "Q" or selection == "q":
                print("Quitting...")
                break

    # Run the stdin listener in the event loop
    loop = asyncio.get_running_loop()
    user_finished = loop.run_in_executor(None, stdin_listener)

    # Wait for user to indicate they are done listening for method calls
    await user_finished

    # Finally, shut down the client
    await device_client.shutdown()


@app.command()
def receive_direct_method(
    verbose: bool = False,
):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    asyncio.run(receive_direct_method_impl())


@app.command()
def upload_to_blob(
    verbose: bool = False,
):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    logger.info("upload_to_blob")


if __name__ == "__main__":
    load_dotenv("iot_hub.env")
    app()
