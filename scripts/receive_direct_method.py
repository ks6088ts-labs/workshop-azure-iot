import asyncio
import logging
from os import getenv

import typer
from azure.iot.device import MethodResponse
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device.iothub.models.methods import MethodRequest
from capture_image import capture_image_from_camera, capture_image_from_file
from dotenv import load_dotenv
from upload_to_blob import upload_to_blob

app = typer.Typer()
logger = logging.getLogger(__name__)


async def receive_direct_method():
    device_client = IoTHubDeviceClient.create_from_connection_string(getenv("IOT_HUB_DEVICE_CONNECTION_STRING"))

    # connect the client.
    await device_client.connect()

    # Define behavior for handling methods
    async def method_request_handler(method_request: MethodRequest):
        logger.info(method_request.name)
        logger.info(method_request.payload)

        if method_request.name == "capture_image_from_file":
            data = capture_image_from_file(
                filename=method_request.payload["filename"],
            )
            response = await upload_to_blob(
                device_client=device_client,
                data=data,
                blob_name=method_request.payload["blob_name"],
            )
            await device_client.send_method_response(
                method_response=MethodResponse.create_from_method_request(
                    method_request=method_request,
                    status=200,
                    payload={
                        "response": response,
                    },
                )
            )
        if method_request.name == "capture_image_from_camera":
            data = capture_image_from_camera(
                index=method_request.payload["index"],
            )
            response = await upload_to_blob(
                device_client=device_client,
                data=data,
                blob_name=method_request.payload["blob_name"],
            )
            await device_client.send_method_response(
                method_response=MethodResponse.create_from_method_request(
                    method_request=method_request,
                    status=200,
                    payload={
                        "response": response,
                    },
                )
            )
        else:
            await device_client.send_method_response(
                method_response=MethodResponse.create_from_method_request(
                    method_request=method_request,
                    status=400,
                    payload={
                        "response": "unknown method",
                    },
                )
            )

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
def main(
    verbose: bool = False,
):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    asyncio.run(receive_direct_method())


if __name__ == "__main__":
    load_dotenv("iot_hub.env")
    app()
