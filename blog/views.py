from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'blog/main.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = 'blog/main.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-published_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'blog/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blog/results.html'