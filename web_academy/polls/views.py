from django.views.generic import DetailView, ListView, UpdateView
from polls.models import Question
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy


class QuestionListView(ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'question_list'


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'


class QuestionUpdateView(UpdateView):
    model = Question


class QuestionCreateView(CreateView):
    model = Question
    fields = ['name']


class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy('question-list')
