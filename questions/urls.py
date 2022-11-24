from django.urls import path
from . import views

app_name = "questions"

urlpatterns = [
    path("", views.question, name="question"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>/", views.detail, name="detail"),
]
