from django.shortcuts import render, get_object_or_404
from .models import Movie, Director
from django.db.models import F, Sum, Max, Min, Avg, Count, Value, IntegerField


# Create your views here.

def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), '-rating')
    movies = Movie.objects.annotate(true_bool=Value(True),
                                    false_bool=Value(False),
                                    str_field=Value('Hello'),
                                    int_field=Value('123'),
                                    new_budget=F('budget') + 100,
                                    sum_field=F('rating') + F('year')
                                    )
    agg = movies.aggregate(Sum('budget'), Avg('rating'), Min('rating'), Max('rating'), Count('name'))
    for movie in movies:
        movie.save()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/directors.html', {
        'directors': directors
    })
