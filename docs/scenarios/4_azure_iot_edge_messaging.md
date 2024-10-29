# Azure IoT Edge Messaging

This scenario demonstrates how to deploy an IoT Edge module.

## Prerequisites

- [Docker](https://www.docker.com/)

## Architecture

[![architecture](https://learn.microsoft.com/azure/iot-edge/media/about-iot-edge/runtime.png?view=iotedge-1.5)](https://learn.microsoft.com/azure/iot-edge/media/about-iot-edge/runtime.png?view=iotedge-1.5)

## Setup

### on Docker container

To run the IoT Edge runtime on a Docker container with Ubuntu 22.04, follow the steps below.

```shell
# set environment variables
export DEVICE_CONNECTION_STRING="HostName=YOUR_IOT_HUB.azure-devices.net;DeviceId=YOUR_DEVICE_ID;SharedAccessKey=YOUR_SHARED_ACCESS_KEY"

# check if the container is running
docker ps

# exec into the container
docker exec -it workshop-azure-iot-iot-edge-1 bash
```

in the container

```shell
# install iot edge runtime
bash install-iot-edge.sh
```

ref. [【ubuntu】Docker で systemctl を使えるようにする](https://zenn.dev/ippe1/articles/327f2b1ed423cb)

### on Azure VM

Deploy Azure VM via Azure Portal with Ubuntu 22.04. See [Create a Linux virtual machine in the Azure portal](https://docs.microsoft.com/azure/virtual-machines/linux/quick-create-portal) for details.

```shell
# SSH into the VM
IP_ADDRESS=111.111.111.111
ssh -i ~/.ssh/id_rsa azureuser@$IP_ADDRESS

# sudo to root
sudo su

# set environment variables
export DEVICE_CONNECTION_STRING="HostName=YOUR_IOT_HUB.azure-devices.net;DeviceId=YOUR_DEVICE_ID;SharedAccessKey=YOUR_SHARED_ACCESS_KEY"

# create an install script (copy and paste install-iot-edge.sh)
cat <<EOF > install-iot-edge.sh

# install iot edge runtime
bash install-iot-edge.sh
```

## Usage

```shell
# help
iotedge -h

# list modules
iotedge list

# monitor logs
iotedge logs SimulatedTemperatureSensor
```

## References

### Azure IoT Edge

- [Create and manage device identities](https://learn.microsoft.com/azure/iot-hub/create-connect-device?tabs=portal)
- [Create and provision an IoT Edge device on Linux using symmetric keys](https://learn.microsoft.com/azure/iot-edge/how-to-provision-single-device-linux-symmetric?view=iotedge-1.4&tabs=azure-portal%2Cubuntu)
- [Azure/iotedge-vm-deploy](https://github.com/Azure/iotedge-vm-deploy)
- [Quickstart: Deploy your first IoT Edge module to a virtual Linux device](https://learn.microsoft.com/azure/iot-edge/quickstart-linux?view=iotedge-1.5)
- [Tutorial: Monitor IoT Edge devices](https://learn.microsoft.com/azure/iot-edge/tutorial-monitor-with-workbooks?view=iotedge-1.5)
