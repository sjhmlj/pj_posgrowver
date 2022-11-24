from django.contrib import admin

# Register your models here.
from .models import Answer, Question, Comment

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Comment)
