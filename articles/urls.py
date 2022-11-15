from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("tech/", views.tech, name="tech"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("writecomment/<int:pk>/", views.writecomment, name="writecomment"),
    path(
        "deletecomment/<int:article_pk>/<int:comment_pk>/",
        views.deletecomment,
        name="deletecomment",
    ),
    path("update/<int:pk>/", views.update, name="update"),
    path("create/", views.create, name="create"),
]
