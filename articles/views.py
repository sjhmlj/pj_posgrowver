from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.http import JsonResponse
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    return render(request, "articles/index.html", context)


from django.utils import timezone


def tech(request):
    articles = Article.objects.all()
    now = timezone.now()
    context = {
        "articles": articles,
        "now": now,
    }
    return render(request, "articles/tech_category.html", context)


def detail(request, pk):
    article = Article.objects.get(id=pk)
    comments = Comment.objects.filter(article=article)
    context = {
        "article": article,
        "comments": comments,
        "commentform": CommentForm(),
        "comments_count": Comment.objects.count(),
    }
    return render(request, "articles/detail.html", context)


import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict


@login_required
def writecomment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.user = request.user
            form.article = article
            form.save()
            model_dict = model_to_dict(form)

            context = {
                "newcomment": json.dumps(model_dict, cls=DjangoJSONEncoder),
                "comments_count": Comment.objects.count(),
            }
            return JsonResponse(context)
