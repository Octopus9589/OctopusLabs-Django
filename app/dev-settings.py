from .settings import *

SECRET_KEY = 'e%kh2#x%jl%ymjx(h458ghti=zi7p^j1kp6_pnpe)s9lp&b9#a'

DEBUG = True

if get_config('REDIS_ENABLED') == 'enabled':
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': "%s:%s/1" % (get_config('REDIS_HOST'), get_config('REDIS_PORT')),
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
            'KEY_PREFIX': 'django_redis'
        }
    }

STRIPE_LIVE_MODE = False