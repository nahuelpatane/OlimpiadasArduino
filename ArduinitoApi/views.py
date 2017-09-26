# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Arduinitos import models
from ArduinitoApi import serializers
from rest_framework import viewsets

class TemperaturaView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Temperatura.objects.all()
    serializer_class = serializers.TemperaturaSerializer

class AguaView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Agua.objects.all()
    serializer_class = serializers.AguaSerializer

class LuzView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Luz.objects.all()
    serializer_class = serializers.LuzSerializer

class InformacionView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Informacion.objects.all()
    serializer_class = serializers.InformacionSerializer
