# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.db import connection, transaction
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
            "courses":Course.objects.all()
    }
    return render(request, 'index.html', context)

def destroy(request, course_id):
    context = {
            "course":Course.objects.get(id=course_id)
    }
    return render(request, 'remove.html', context)

def add(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error,extra_tags=tag)
    else:
        Course.objects.create(name=request.POST['name'],description=request.POST['description'])
    return redirect('/')

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/')
