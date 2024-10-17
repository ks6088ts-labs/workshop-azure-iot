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

```shell
# Clone the repository
$ git clone https://github.com/ks6088ts-labs/workshop-azure-iot.git

# Change the directory
$ cd workshop-azure-iot

# Prepare the environment files based on the templates
$ find . -maxdepth 1 -name "*.env.template" -exec sh -c 'cp "$1" "${1%.env.template}.env"' _ {} \;

# Update the environment files with your values

# Run CI test locally to check the environment
make ci-test

# Deploy Azure Functions resources
$ bash scripts/deploy_azure_functions_resources.sh

# Publish Azure Functions
$ export FUNCTION_APP_NAME=adhoc-azure-functions-RANDOM_SUFFIX
$ bash scripts/publish_azure_functions.sh
```

## References

### Azure Functions

Run the function app locally

```shell
# Run the function app locally with the Azure Functions Core Tools
$ poetry run func start
```

Deploy the function app to Azure

```shell
# Deploy resources to Azure
$ bash scripts/deploy_azure_functions_resources.sh

$ export FUNCTION_APP_NAME="CHANGE_ME"

# Publish the function app to Azure
$ bash scripts/publish_azure_functions.sh
```

- [Using FastAPI Framework with Azure Functions](https://learn.microsoft.com/en-us/samples/azure-samples/fastapi-on-azure-functions/fastapi-on-azure-functions/)
