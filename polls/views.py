from django.http.response import Http404, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Choice, Question
from django.db.models import F
from django.urls import reverse
from django.utils import timezone

# Create your views here.
def index(request):
    polls_list = Question.objects.all().order_by('pub_date')
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
        selected_choice = question.choice_set.filter(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.update(votes = F('votes') + 1)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def recent(request):
    polls_list = Question.objects.all().order_by('-pub_date')[:5]
    return render(request,'polls/recent-polls.html',{'polls_list':polls_list})

def create(request):
    if request.method == "POST":
        question_text = request.POST.get('question_text')
        choice1 = request.POST.get('choice1')
        choice2 = request.POST.get('choice2')
        choice3 = request.POST.get('choice3')
        choice4 = request.POST.get('choice4')
        q = Question.objects.create(question_text=question_text,pub_date=timezone.now())
        q.choice_set.create(choice_text = choice1,votes = 0)
        q.choice_set.create(choice_text = choice2,votes = 0)
        q.choice_set.create(choice_text = choice3,votes = 0)
        q.choice_set.create(choice_text = choice4,votes = 0)
        try:
            return JsonResponse({
                "status" : 200,
                "data":{
                    "question_id":q.id,
                    "question_text":q.question_text,
                    "choices":[choice1,choice2,choice3,choice4]
                }
            })
        except:
            return Http404()
    return render(request,'polls/create-poll.html')