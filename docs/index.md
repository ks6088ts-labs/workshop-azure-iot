# References

## Azure Functions

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

### References

- [Using FastAPI Framework with Azure Functions](https://learn.microsoft.com/en-us/samples/azure-samples/fastapi-on-azure-functions/fastapi-on-azure-functions/)
