from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Choice, Question
from django.db.models import F
from django.urls import reverse
# Create your views here.
def index(request):
    polls_list = Question.objects.all().order_by('pub_date')
    response = ', '.join([q.question_text for q in polls_list])
    return render(request,'polls/index.html',{'polls_list':polls_list})

def details(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/details.html',{'question':question})

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/result.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))