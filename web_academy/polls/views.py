from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from polls.models import Question

@require_http_methods(["GET","POST"])
def index(request):
	template = loader.get_template('polls/index.html')

	if request.POST:
		print(request.POST)
		r_data = request.POST
		data = {'question_text': r_data.get('question_text'),
		 		'pub_date': r_data.get('pub_date')}
		try:
			Question.objects.create(question_text=data['question_text'],
									pub_date=data['pub_date'])
		except Exception, e:
			context = RequestContext(request, {
				'error': str(e)
				})
			return HttpResponse(template.render(context))
		return redirect(reverse('polls:index'))

	query_question_text = request.GET.get('question_text', None)

	if query_question_text:
			questions = Question.objects.filter(
				question_text__icontains=query_question_text)
	else:
		questions = Question.objects.all()

	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'questions_list': questions,
	})
	return HttpResponse(template.render(context))

def detail(request, q_id):
	question = Question.objects.get(id=q_id)
	return HttpResponse(str(question.question_text))