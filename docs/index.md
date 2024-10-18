# workshop-azure-iot

This repository is for a workshop using Azure IoT services.

## Prerequisites

To run all the projects in this repository, you need the followings.

- [Python 3.10+](https://www.python.org/downloads/)
<!-- add services here -->

Here are the preferred tools for development.

- [Poetry](https://python-poetry.org/docs/#installation)
- [GNU Make](https://www.gnu.org/software/make/)

## Scenarios

- [Azure IoT Hub Messaging](scenarios/1_azure_iot_hub_messaging)

## Setup

### Infrastructure

Click the button below to deploy the infrastructure to Azure.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fks6088ts-labs%2Fbaseline-environment-on-azure-bicep%2Frefs%2Fheads%2Fmain%2Finfra%2Fscenarios%2Fworkshop-azure-iot%2Fazuredeploy.json)

### Application

#### Setup environment variables

To get started, you have to set environment variables in the `*.env` files in the root directory.
Please refer to the `*.env.template` files for the required environment variables.

```shell
# Clone the repository
$ git clone https://github.com/ks6088ts-labs/workshop-azure-iot.git

# Change the directory
$ cd workshop-azure-iot

# Prepare the environment files based on the templates
$ make env
```

Please update the environment files to fit your environment.

#### How to run

**Connection test**

Following commands are for testing the connection to the Azure resources.
Passing the test means the environment is set up correctly.

```shell
# Run test locally to check the environment is set up correctly
$ make test
```

**Run FastAPI server locally**

```shell
# Install dependencies
$ make install-deps

# Run FastAPI server locally
$ make server
```

**Run FastAPI server locally from Docker image**

Docker is required to run the FastAPI server locally from the Docker image.
The image for this project is available on Docker Hub.
See the Docker Hub repository: [ks6088ts/workshop-azure-iot](https://hub.docker.com/repository/docker/ks6088ts/workshop-azure-iot/general).

```shell
# Run FastAPI server locally from Docker image
$ make docker-run
```

**Run Azure Functions locally**

```shell
# Run Azure Functions locally
$ make azure-functions
```

**Deploy Azure Functions**

```shell
# Deploy Azure Functions resources
$ make azure-functions-deploy

# Publish Azure Functions
$ export FUNCTION_APP_NAME=adhoc-azure-functions-RANDOM_SUFFIX
$ make azure-functions-publish
```

## References

### Azure Functions

- [Using FastAPI Framework with Azure Functions](https://learn.microsoft.com/en-us/samples/azure-samples/fastapi-on-azure-functions/fastapi-on-azure-functions/)
