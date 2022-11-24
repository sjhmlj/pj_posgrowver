from django.shortcuts import render, redirect
from .models import Question, Comment
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, CommentForm

# Create your views here.
def question(request):
    questions = Question.objects.all()
    context = {
        "questions": questions,
    }
    return render(request, "questions/question.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect("questions:question")

    context = {"form": QuestionForm()}
    return render(request, "questions/create.html", context)


def detail(request, pk):
    question = Question.objects.get(id=pk)
    comments = Comment.objects.filter(question=question)
    context = {
        "question": question,
        "comments": comments,
        "commentform": CommentForm(),
        "comments_count": Comment.objects.filter(question=question).count(),
    }
    return render(request, "questions/detail.html", context)
