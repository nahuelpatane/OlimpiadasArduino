# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Temperatura)
admin.site.register(Agua)
admin.site.register(Luz)
admin.site.register(Hora)
admin.site.register(Informacion)
