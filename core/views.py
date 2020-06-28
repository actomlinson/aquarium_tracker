from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Aquarium

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, aquarium_id):
    aquarium = get_object_or_404(Aquarium, pk=aquarium_id)
    return HttpResponse("Info on %s." % aquarium.nickname)

#def detail(request, question_id):
    #try:
        #question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
        #raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})
