
from films_dict.models import Movie
from films_dict.views import MovieListView


class IndexView(MovieListView):
    title = "Welcome to movies dictionary!"
    template_name = 'index.html'
    model = Movie