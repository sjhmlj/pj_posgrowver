from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("tech/", views.tech, name="tech"),
    path("tech_html/", views.tech_html, name="tech_html"),
    path("tech_css/", views.tech_css, name="tech_css"),
    path("tech_js/", views.tech_js, name="tech_js"),
    path("tech_django/", views.tech_django, name="tech_django"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("writecomment/<int:pk>/", views.writecomment, name="writecomment"),
    path(
        "deletecomment/<int:article_pk>/<int:comment_pk>/",
        views.deletecomment,
        name="deletecomment",
    ),
    path("update/<int:pk>/", views.update, name="update"),
    path("create/", views.create, name="create"),
    path("deletearticle/<int:pk>/", views.deletearticle, name="deletearticle"),
    path("question/", views.question, name="question"),
]
