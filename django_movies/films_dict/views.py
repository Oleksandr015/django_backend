from django.shortcuts import render

# Create your views here.
from films_dict.models import Movie, AGE_LIMIT_CHOICES
from films_dict.models import Genre


def hello(request):
    return render(
        request,
        template_name="hello.html",
        context={'adjectives': ['beautiful', 'cruel', 'wonderful']}
    )


def movies(request):
    return render(
        request,
        template_name="movies.html",
        context={'movies': Movie.objects.all()},
    )


def genres(request):
    return render(
        request,
        template_name="genres.html",
        context={'genres': Movie.objects.filter(genre__age_limit__lt=AGE_LIMIT_CHOICES.Adults)},
    )
