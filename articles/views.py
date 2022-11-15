from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.http import JsonResponse
from .forms import CommentForm, ArticleForm
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
        "comments_count": Comment.objects.filter(article=article).count(),
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
                "user": str(request.user.username),
            }
            return JsonResponse(context)


@login_required
def deletecomment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    Comment.objects.get(id=comment_pk).delete()
    context = {}
    return JsonResponse(context)


@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST" and request.user == article.user:
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail", pk)

    context = {
        "form": ArticleForm(instance=article),
        "article": article,
    }
    return render(request, "articles/update.html", context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("articles:detail", article.id)

    context = {"form": ArticleForm()}
    return render(request, "articles/create.html", context)
