from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    intro = models.TextField()
    body = models.TextField()
    hashtag = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(get_user_model(), related_name="like_articles")
    bookmark = models.ManyToManyField(get_user_model())
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="articles"
    )


class Answer(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(get_user_model(), related_name="like_answers")


class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    like_users = models.ManyToManyField(get_user_model(), related_name="like_comments")
    comments = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
