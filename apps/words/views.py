# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
    if request.session.get('words') == None:
        request.session['words'] = []
    return render(request, 'words/index.html')

def add_word(request):
    word = request.POST['word']
    color = request.POST['color']
    if 'fonts' in request.POST:
        font = "big"
    else:
        font = "normal"

    time_added = datetime.strftime(datetime.now(), "%H:%M:%S %p, %B %d, %Y")
    request.session['words'].append({'word': word, 'color': color, 'font': font, 'added': time_added})
    request.session.modified = True
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')