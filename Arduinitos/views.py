# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def verhome(request):
    return render_to_response('index.html',{},RequestContext(request))
