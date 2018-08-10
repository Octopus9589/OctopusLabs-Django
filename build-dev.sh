#!/bin/bash

set -e

echo "docker build \
-t django-dev:develop . -f Dockerfile-dev"

docker build \
-t django-dev:develop . -f Dockerfile-dev