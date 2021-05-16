from django.shortcuts import render
from django.http import HttpResponse 
from .models import Question
# Create your views here.
def index(request):
    polls_list = Question.objects.all().order_by('pub_date')
    response = ', '.join([q.question_text for q in polls_list])
    return HttpResponse(response)

def details(request, question_id):
    return HttpResponse("details page")

def results(request, question_id):
    return HttpResponse("results page")

def vote(request, question_id):
    return HttpResponse("votes action")