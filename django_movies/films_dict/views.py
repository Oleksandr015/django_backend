from django import views
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from films_dict.models import Movie, AGE_LIMIT_CHOICES

from films_dict.models import Genre


class HelloView(views.View):
    def hello(request):
        return render(
            request,
            template_name="hello.html",
            context={'adjectives': ['beautiful', 'cruel', 'wonderful']}
        )


class MovieView(TemplateView):
    template_name = "movies.html"
    extra_context = {
        'movies': Movie.objects.all(),
        'limits': AGE_LIMIT_CHOICES,
    }


class GenreView(ListView):
    template_name = "genres.html"
    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['AGE_LIMIT_CHOICES'] = Genre.objects.all()
        return context
