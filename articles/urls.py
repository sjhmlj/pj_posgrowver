from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("tech/", views.tech, name="tech"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("writecomment/<int:pk>/", views.writecomment, name="writecomment"),
]
