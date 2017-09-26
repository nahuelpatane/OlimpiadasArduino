# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Temperatura(models.Model):
    id_temp = models.AutoField(primary_key=True)
    valor= models.IntegerField("valor", null=False)
    unidad= models.CharField(max_length=32, default="°C")
    estado= models.NullBooleanField(default=False, blank=True,null=True)

class Agua(models.Model):
    id_agua = models.AutoField(primary_key=True)
    valor= models.IntegerField("valor", null=False)
    unidad= models.CharField(max_length=32, default="l")
    estado= models.NullBooleanField(default=False, blank=True,null=True)

class Luz(models.Model):
    id_luz = models.AutoField(primary_key=True)
    valor= models.IntegerField("valor", null=False)
    unidad= models.CharField(max_length=32, default="lm")
    estado= models.NullBooleanField(default=False, blank=True,null=True)

class Hora(models.Model):
    id_hora = models.AutoField(primary_key=True)
    hora= models.TimeField()
    temperatura = models.ForeignKey(Temperatura, on_delete=models.CASCADE)
    agua = models.ForeignKey(Agua, on_delete=models.CASCADE)
    luz = models.ForeignKey(Luz, on_delete=models.CASCADE)

class Informacion(models.Model):
    id_info = models.AutoField(primary_key=True)
    fecha= models.DateField("fecha")
    hora = models.ForeignKey(Hora, on_delete=models.CASCADE)


