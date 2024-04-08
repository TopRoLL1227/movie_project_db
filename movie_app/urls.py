from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path("", views.show_all_movie),
    path("movie/<int:id_movie>", views.show_one_movie, name='movie_detail'),
]