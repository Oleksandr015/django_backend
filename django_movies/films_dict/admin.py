from django.contrib import admin

from films_dict.models import Movie
from films_dict.models import Genre

admin.site.register(Movie)
admin.site.register(Genre)

# Register your models here.

