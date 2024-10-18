#!/bin/sh

set -eux

find . -maxdepth 1 -name "*.env.template" -exec sh -c 'cp "$1" "${1%.env.template}.env"' _ {} \;
