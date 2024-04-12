from django.urls import path
from django.http import HttpResponse
from . import views
from django.contrib import admin

admin.site.site_header = 'Адмінка'
admin.site.index_title = 'Супер адмінка'

urlpatterns = [
    path("", views.show_all_movie),
    path("movie/<slug:slug_movie>", views.show_one_movie, name='movie_detail'),
]