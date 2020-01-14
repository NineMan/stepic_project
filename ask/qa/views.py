from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from qa.models import *
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


def test(request, *args, **kwargs):
	return HttpResponse('OK')


def main(request):
	limit = 10
	try:
		page = int(request.GET.get("page", 1))
	except ValueError:
		page = 1
	questions = Question.objects
	questions = questions.order_by("added_at")            # here sorting on the main page
	paginator = Paginator(questions, limit)
	paginator.baseurl = "/?page="
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return render(request, "main_page.html", {
		'questions': page.object_list,
		'paginator': paginator, 
		'page': page,
	})


def popular(request):
	limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		page = 1
	questions = Question.objects.order_by("-rating")
	paginator = Paginator(questions, limit)
	paginator.baseurl = "/popular/?page="
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return render(request, "popular_page.html", {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
	})


def question(request, question_id):

	q = get_object_or_404(Question, id=question_id)
	answers = Answer.objects.all().filter(question = q)

	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save(request.user)
			url = q.get_url()
#			url = '/question/' + str(question_id) + '/'
			return HttpResponseRedirect(url)
	else:
		form = AnswerForm({'question': q})

	return render(request, "question_page.html", {
		'question': q,
		'answers': answers,
		'form': form,
	})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


def answer(request):
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save()
			q_id = answer.question_id
			question = get_object_or_404(Question, pk=q_id)
			url = question.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AnswerForm()
	return render(request, 'question_page.html', {
		'form': form
	})


def signup(request):
	if request.method == "POST":
		print('1')
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username = user.username, password = request.POST['password'])	
			auth_login(request, user)
			return HttpResponseRedirect('/')
	else:
		print('2')
		form = SignupForm()
	return render(request, 'signup.html', {'form': form})


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.save()
			if user:
				auth_login(request, user)
				return HttpResponseRedirect('/')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form' : form})
