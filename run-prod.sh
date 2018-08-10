#!/bin/bash

set -e

echo "populate prod ------>"

gunicorn --bind 0.0.0.0:5000 app.wsgi:application --log-level debug
