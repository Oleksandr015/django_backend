from django.contrib import admin

from films_dict.models import Movie, Director, Country, Genre

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Director)

# Register yr models here.

