#!/bin/sh

set -eux

poetry export -f requirements.txt -o requirements.txt --without-hashes

func azure functionapp publish $FUNCTION_APP_NAME
