# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from profiles import libs as profile_libs

def index(request, path=None):
    response = HttpResponse('blah')

    profile_libs.generate_anonymous_user(request, response)
    return render(request, 'index.html')
