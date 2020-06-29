from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Aquarium
from django.views import generic

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, aquarium_id):
    aquarium = get_object_or_404(Aquarium, pk=aquarium_id)
    return render(request, 'aquarium_detail.html', {'aquarium': aquarium})

class DetailView(generic.DetailView):
    model = Aquarium
    template_name = 'aquarium_detail.html'


