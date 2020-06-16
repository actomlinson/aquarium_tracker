from django.shortcuts import render

def detail(request, aquarium_id, aquarium_nickname):
    return HttpResponse("Info on %s." % aquarium_nickname)
