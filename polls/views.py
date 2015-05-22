from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, HttpResponse
from polls.models import Question, Choice, Run, Runner
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import NameForm

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'
  def get_queryset(self):
    return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
  model = Question
  template_name ='polls/detail.html'

class ResultsView(generic.DetailView):
  model = Question
  template_name ='polls/results.html'

class RunView(generic.DetailView):
  model = Run
  template_name = 'polls/run.html'

def run(request):
  p = Run(distance=1.0, time=30, run_date=timezone.now(), color="green")
  p.save();  


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = form.cleaned_data
            p = Runner(name=data['your_name']); 
            p.save();
            return HttpResponseRedirect("")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})


def vote(request, pk):
  p = get_object_or_404(Question, pk=pk)
  try: 
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question' : p,
      'error_message': "You didn't select a choice.",
    })
  else:
    selected_choice.votes +=1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


#####################################################
#### functions below not necessarily used
# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5] 
  ## a json :) output ayaya
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id) 
  return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id): 
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})

def thanks(request):
  return HttpResponse("Thanks!")
