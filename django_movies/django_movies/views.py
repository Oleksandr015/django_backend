from django_movies.films_dict.models import Movie
from django_movies.films_dict.views import MovieListView


class IndexView(MovieListView):
    title = "Welcome to momies dictionary!"
    template_name = 'index.html'
    model = Movie