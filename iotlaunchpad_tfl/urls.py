from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'iotlaunchpad_tfl.views.home', name='home'),
    url(r'^data/bus-stops$', 'iotlaunchpad_tfl.views.bus_stops'),
]
