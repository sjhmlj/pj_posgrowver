from .models import Answer, Question, Comment
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        exclude = ["bookmark", "like_users", "user"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            "content",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
