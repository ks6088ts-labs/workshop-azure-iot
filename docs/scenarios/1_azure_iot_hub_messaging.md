# Azure IoT Hub Messaging

This scenario demonstrates how to handle messages from an Azure IoT Hub using the Azure IoT Hub SDK for Python.

## Architecture

[![architecture](../assets/1_architecture.png)](../assets/1_architecture.png)

## Setup

### Configure IoT Hub file uploads via Azure Portal

After you deploy the Azure IoT Hub, you need to configure IoT Hub file uploads. This is required to upload files from the IoT Hub to the Azure Blob Storage.
Here are the steps to configure IoT Hub file uploads: [Configure IoT Hub file uploads using the Azure portal](https://learn.microsoft.com/azure/iot-hub/iot-hub-configure-file-upload)

It is recommended to use managed identities to access the Azure Blob Storage from the Azure IoT Hub. See how to configure managed identities for IoT Hub: [Configure file upload with managed identities](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-managed-identity?tabs=portal#configure-file-upload-with-managed-identities)

### Configure Azure Cosmos DB as a routing endpoint

To pass messages from the Azure IoT Hub to the Azure Cosmos DB, you need to configure Azure Cosmos DB as a routing endpoint.

- [General Availability: Azure IoT Hub supports Azure Cosmos DB routing endpoint now!](https://techcommunity.microsoft.com/t5/internet-of-things-blog/general-availability-azure-iot-hub-supports-azure-cosmos-db/ba-p/3945877)
- [IoT Hub endpoints > Azure Cosmos DB as a routing endpoint](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-endpoints#azure-cosmos-db-as-a-routing-endpoint)
- [IoT Hub support for managed identities](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-managed-identity?WT.mc_id=Portal-Microsoft_Azure_IotHub&tabs=portal)

## Edge device

To understand how to use the Azure IoT Hub SDK for Python, we provide a script which is supposed to run on the edge device. This demonstrates how to utilize the SDK to send and receive messages from the Azure IoT Hub.
To implement features around the Azure IoT Hub, you can refer to the following scripts.

- [Samples for the Azure IoT Hub Device SDK](https://github.com/Azure/azure-iot-sdk-python/tree/main/samples)

### Upload a file to the Azure Blob Storage

```shell
$ poetry run python scripts/upload_to_blob.py --verbose \
    --file-path ./README.md \
    --blob-name README.md
```

[upload_to_blob.py](https://github.com/Azure/azure-iot-sdk-python/blob/main/samples/async-hub-scenarios/upload_to_blob.py) is a sample code provided by the Azure IoT SDK for Python.

### Capture image

To capture an image from the camera module, you need to run the following command from the edge device.
From the development point of view, it would be better to use a video file to mock the camera module.
So, we provide a script that captures an image from a video file or camera.
Download [vtest.avi](https://github.com/opencv/opencv/blob/4.x/samples/data/vtest.avi) to use it as a video file.

```shell
# From video file to mock camera
$ poetry run python scripts/capture_image.py file --verbose \
    --filename ./docs/assets/vtest.avi \
    --outfile ./docs/assets/image.jpg

# From camera
$ poetry run python scripts/capture_image.py camera --verbose \
    --index 0 \
    --outfile ./docs/assets/image.jpg
```

### Receive direct method requests

To receive direct method requests, you need to run the following command from edge device.
This script handles direct method requests from the Azure IoT Hub.

```shell
$ poetry run python scripts/receive_direct_method.py --verbose
```

[receive_direct_method.py](https://github.com/Azure/azure-iot-sdk-python/blob/main/samples/async-hub-scenarios/receive_direct_method.py) is a sample code provided by the Azure IoT SDK for Python.

## Cloud

Run API server locally to provide RESTful APIs for the edge device.

```shell
$ make server
```

## Demo

### Setup

1. Run the API server. (on local, Docker, or Azure Functions etc.)

```shell
$ make server
```

2. Run the edge device script to receive direct method requests.

```shell
$ poetry run python scripts/receive_direct_method.py --verbose
```

### Send a request to the API server to call the direct method.

Go to docs url which shows Swagger UI and send a request to the API server to call the direct method.

1. Call the direct method from API server.

From the Swagger UI, call `POST /iot_hub/call_direct_method` with the following request body.

| method_name               | payload                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| capture_image_from_file   | {"filename": "./docs/assets/1_architecture.png", "blob_name": "file.png"} |
| capture_image_from_camera | {"index": 0, "blob_name": "capture0.png"}                                 |

2. Check the result.

From the Swagger UI, call `GET /blob_storage` to check the uploaded file.

3. Get the uploaded file.

Call `GET /blob_storage/images/{device_name}/{file_name}` to get the uploaded file.

4. Explain the image by Azure OpenAI API.

Call `POST /ai_services/chat/completions_with_image` with the following request body.

- `prompt`: The prompt to send to the OpenAI API.
- `file`: The image file to send to the Azure OpenAI API.

### Play with Device Twin

1. Update the device twin.

- `GET /iot_hub/device_twin` to get the device twin.

2. Check the updated device twin.

- `PATCH /iot_hub/device_twin` to update the device twin.
