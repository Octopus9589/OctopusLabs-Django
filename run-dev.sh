#!/bin/bash

set -e

pipenv install --dev

source $(pipenv --venv)/bin/activate

python manage.py migrate

echo "populate dev ------>"

python manage.py runserver 0.0.0.0:$PORT
