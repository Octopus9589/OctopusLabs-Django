#!/bin/bash

while IFS='=' read -r key value; do
  if [[ "$key" != *#* ]]; then
    export "HELM_"$key=$value
  fi
done < .env

while IFS='=' read -r key value; do
  if [[ "$key" != *#* ]]; then
    export "HELM_"$key=$value
  fi
done < .env-prod

# print exported HELM_*
env | grep HELM_

