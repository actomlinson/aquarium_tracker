from django.shortcuts import render
from django.http import HttpResponse
from .models import Tank

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, aquarium_id):
    try:
        t = Tank.objects.get(pk=aquarium_id)
    except:
        return HttpResponse("Tank doesn't exist")
    return HttpResponse("Info on %s." % t.nickname)
