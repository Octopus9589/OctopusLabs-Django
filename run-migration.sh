#!/bin/bash

set -e

echo "migrate ------>"

python manage.py migrate

echo "stripe init ------>"

python manage.py djstripe_init_customers

python manage.py djstripe_sync_plans_from_stripe