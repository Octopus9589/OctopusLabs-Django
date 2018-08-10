import datetime

import os

import djstripe

from django.shortcuts import render

from django.http import HttpResponse

from django.conf import settings

from django.core.cache import cache

from django.contrib.auth.models import User

from django.http import JsonResponse

from django.core import serializers


def index(request):
  if os.environ.get('DEV_MODE', None):
    return HttpResponse('running in local')

  return HttpResponse('running in production')

def mysql(request):
  user_list = serializers.serialize('json', User.objects.all())

  return HttpResponse("Throw no error! The app have been connected to mysql server successfuly")

def memcached(request):
  if os.environ.get('MEMCACHED_ENABLED', None) != 'enabled':
    return HttpResponse('Not implemented!')

  timestamp = datetime.datetime.today().timestamp()

  if cache.get('memcached_key') is None:
    cache.set('memcached_key', timestamp, 10) # 10 seconds

  return HttpResponse("You've seen me at %s, please remember it! - Memcached" % cache.get('memcached_key'))

def redis(request):
  if os.environ.get('REDIS_ENABLED', None) != 'enabled':
    return HttpResponse('Not implemented!')

  timestamp = datetime.datetime.today().timestamp()

  if cache.get('redis_key') is None:
    cache.set('redis_key', timestamp, 10) # 10 seconds

  return HttpResponse("You've seen me at %s, please remember it! - Redis" % cache.get('redis_key'))

def stripe_test(request):
  print(dir(djstripe))
  # customer = djstripe.Customer.create(
  #   email='paying.user@example.com',
  #   source='tok_mastercard',
  # )

  return HttpResponse(dir(djstripe))