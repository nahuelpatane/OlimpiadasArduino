# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect

# Create your views here.

def VerHome(request):
    return render_to_response('index.html',{},RequestContext(request))

def VerTemp(request):
    return render_to_response('temperatura.html',{},RequestContext(request))

def VerLuz(request):
    return render_to_response('luz.html',{},RequestContext(request))

def VerAgua(request):
    return render_to_response('agua.html',{},RequestContext(request))