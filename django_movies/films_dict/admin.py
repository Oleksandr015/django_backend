from django.contrib import admin

from django_movies.films_dict.models import Movie

admin.films_dict.register(Movie)

# Register your models here.
