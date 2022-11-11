from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    like_users = models.ManyToManyField(get_user_model(), related_name="like_articles")
    bookmark = models.ManyToManyField(get_user_model())


class Answer(models.Model):
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(get_user_model(), related_name="like_answers")


class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(get_user_model(), related_name="like_comments")
    comments = models.ForeignKey("self", on_delete=models.CASCADE)
