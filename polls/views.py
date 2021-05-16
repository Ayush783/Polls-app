from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def index(request):
    return HttpResponse("Index page")

def details(request, question_id):
    return HttpResponse("details page")

def results(request, question_id):
    return HttpResponse("results page")

def vote(request, question_id):
    return HttpResponse("votes action")