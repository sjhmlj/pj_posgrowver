from django.contrib import admin

# Register your models here.
from .models import Article, Comment, Cheer

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Cheer)
