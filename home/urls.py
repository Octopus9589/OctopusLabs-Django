from django.urls import path, include

from . import views

urlpatterns = [
  path('', views.index, name='index'),

  path('memcached/', views.memcached, name='memcached'),
  path('redis/', views.redis, name='redis'),
  path('mysql/', views.mysql, name='mysql'),
  path('stripe-test/', views.stripe_test, name='stripe_test'),
  path('stripe/', include('djstripe.urls', namespace='djstripe')),
]