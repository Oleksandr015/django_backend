import logging

from django import views
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView
from films_dict.models import Movie, AGE_LIMIT_CHOICES, Genre

from films_dict.forms import MovieForm


class HelloView(views.View):
    def hello(request):
        return render(
            request,
            template_name="hello.html",
            context={'adjectives': ['beautiful', 'cruel', 'wonderful']}
        )


class MovieView(ListView):
    template_name = "movies.html"
    model = Movie

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['limits'] = AGE_LIMIT_CHOICES

        return result


class GenreView(ListView):
    template_name = "genres.html"
    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['AGE_LIMIT_CHOICES'] = Genre.objects.all()
        return context


LOGGER = logging.getLogger()


class MovieCreateView(CreateView):
    title = 'Add Movie'
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_create')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title=cleaned_data['title'],
            genre=cleaned_data['genre'],
            rating=cleaned_data['rating'],
            released=cleaned_data['released'],
            description=cleaned_data['description'],
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided')
        return super().form_invalid(form)


class MovieUpdateView(UpdateView):
    title = 'Update Movie'
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided')
        return super().form_invalid(form)

