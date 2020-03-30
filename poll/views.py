from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Question
from .forms import QuestionForm


def home(request):

    question = Question.objects.all()
    context = {'question': question}
    return render(request, 'poll/home.html', context)


def vote(request, id):
    question = Question.objects.get(pk=id)

    if request.method == 'POST':

        selected_option = request.POST['question']

        if selected_option == 'option1':
            question.option1_votes += 1
        elif selected_option == 'option2':
            question.option2_votes += 1
        elif selected_option == 'option3':
            question.option3_votes += 1
        else:
            return HttpResponse(400, 'Invalid form')

        question.save()
        return redirect('results', question.id)

    context = {
        'question': question
    }
    return render(request, 'poll/vote.html', context)


def results(request, id):
    question = Question.objects.get(pk=id)
    context = {'question': question}
    return render(request, 'poll/results.html', context)


def create(request):
    myform = QuestionForm()

    if request.method == 'POST':
        myform = QuestionForm(request.POST)
        if myform.is_valid():
            myform.save()
        return redirect('home')

    context = {'form': myform}
    return render(request, 'poll/create.html', context)
