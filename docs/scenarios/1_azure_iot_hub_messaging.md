# Azure IoT Hub Messaging

This scenario demonstrates how to handle messages from an Azure IoT Hub using the Azure IoT Hub SDK for Python.

## Setup

After you deploy the Azure IoT Hub, you need to configure IoT Hub file uploads. This is required to upload files from the IoT Hub to the Azure Blob Storage.
Here are the steps to configure IoT Hub file uploads: [Configure IoT Hub file uploads using the Azure portal](https://learn.microsoft.com/azure/iot-hub/iot-hub-configure-file-upload)

## Scenarios

To understand how to use the Azure IoT Hub SDK for Python, we provide a script that demonstrates how to utilize the SDK to send and receive messages from the Azure IoT Hub.

### Receive direct method requests

To receive direct method requests, you need to run the following command from edge device.
This script handles direct method requests from the Azure IoT Hub.

```shell
$ poetry run python scripts/receive_direct_method.py --verbose
```

[receive_direct_method.py](https://github.com/Azure/azure-iot-sdk-python/blob/main/samples/async-hub-scenarios/receive_direct_method.py) is a sample code provided by the Azure IoT SDK for Python.

### Upload a file to the Azure Blob Storage

```shell
$ poetry run python scripts/upload_to_blob.py --verbose \
    --file-path ./README.md \
    --blob-name README.md
```
