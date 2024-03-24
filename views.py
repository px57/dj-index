# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from index.decorators import load_languages
from profiles import libs as profile_libs
import os

@load_languages
def index(request, path=None):
    # response = HttpResponse('blah')
    # profile_libs.generate_anonymous_user(request, response)

    try:
        return render(request, request.language.get_index_src())
    except Exception as e:
        return render(request, 'index.html')