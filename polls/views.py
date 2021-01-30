from django.shortcuts import get_object_or_404 ,render
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
#Importamos los modelos para acceder a sus datos
from .models import Questions,Choice

# Create your views here.
#def index(request):
    #return HttpResponse("Hello, World. Probando Python y Django.")
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.order_by('-pub_date')[:5]
    

class DetailView(generic.DetailView):
    #formas de mostrar un 404
    #forma 1
    #try:
        #question = Questions.objects.get(pk=question_id)
    #except Questions.DoesNotExist:
        #raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})
    #forma 2
    #question = get_object_or_404(Questions, pk=question_id)
    #return render(request, 'polls/detail.html', {'question': question})
    model = Questions
    context_object_name = 'question'
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'



def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})