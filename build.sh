#!/bin/bash

set -e

echo "docker build \
-t django-dev:latest . -f Dockerfile"

docker build \
-t django-dev:latest . -f Dockerfile