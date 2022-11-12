from django.shortcuts import render
from .models import Article


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
    context = {
        "article": article,
    }
    return render(request, "articles/detail.html", context)
