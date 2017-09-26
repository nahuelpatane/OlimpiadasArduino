from django.conf.urls import *
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('Arduinitos.urls', namespace='ardu' )),
    url(r'', include('ArduinitoApi.urls', namespace='arduapi')),
]

