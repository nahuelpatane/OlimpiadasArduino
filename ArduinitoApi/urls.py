#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from ArduinitoApi import views
from rest_framework.routers import DefaultRouter

app_name = 'arduinitoapi'

router = DefaultRouter()
router.register(r'temperatura', views.TemperaturaView)
router.register(r'agua', views.AguaView)
router.register(r'luz', views.LuzView)
router.register(r'hora', views.HoraView)
router.register(r'informacion', views.InformacionView)

urlpatterns = [
               url(r'^api/', include(router.urls, namespace='api')),
               ]
