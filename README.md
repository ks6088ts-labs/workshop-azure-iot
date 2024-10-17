[![test](https://github.com/ks6088ts-labs/workshop-azure-iot/actions/workflows/test.yaml/badge.svg?branch=main)](https://github.com/ks6088ts-labs/workshop-azure-iot/actions/workflows/test.yaml?query=branch%3Amain)
[![docker](https://github.com/ks6088ts-labs/workshop-azure-iot/actions/workflows/docker.yaml/badge.svg?branch=main)](https://github.com/ks6088ts-labs/workshop-azure-iot/actions/workflows/docker.yaml?query=branch%3Amain)
[![docker-release](https://github.com/ks6088ts-labs/workshop-azure-iot/actions/workflows/docker-release.yaml/badge.svg)](https://github.com/ks6088ts-labs/workshop-azure-iot/actions/workflows/docker-release.yaml)
[![ghcr-release](https://github.com/ks6088ts-labs/workshop-azure-iot/actions/workflows/ghcr-release.yaml/badge.svg)](https://github.com/ks6088ts-labs/workshop-azure-iot/actions/workflows/ghcr-release.yaml)
[![github-pages](https://github.com/ks6088ts-labs/workshop-azure-iot/actions/workflows/github-pages.yaml/badge.svg)](https://github.com/ks6088ts-labs/workshop-azure-iot/actions/workflows/github-pages.yaml)

<!-- https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-azure-button -->

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fks6088ts-labs%2Fbaseline-environment-on-azure-bicep%2Frefs%2Fheads%2Fmain%2Finfra%2Fscenarios%2Fworkshop-azure-iot%2Fazuredeploy.json)

# workshop-azure-iot

This is a template repository for Python

## Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [GNU Make](https://www.gnu.org/software/make/)

## Development instructions

### Local development

Use Makefile to run the project locally.

```shell
# help
make

# install dependencies for development
make install-deps-dev

# run tests
make test

# run CI tests
make ci-test
```

### Docker development

```shell
# build docker image
make docker-build

# run docker container
make docker-run

# run CI tests in docker container
make ci-test-docker
```

To publish the docker image to Docker Hub, you need to set the following secrets in the repository settings.

```shell
gh secret set DOCKERHUB_USERNAME --body $DOCKERHUB_USERNAME
gh secret set DOCKERHUB_TOKEN --body $DOCKERHUB_TOKEN
```
