from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('ArduinitoApi.urls', namespace = "arduapi")),
    url(r'^admin/', include(admin.site.urls)),
]
