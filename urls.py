"""django_movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from films_dict.views import MovieView, HelloView, GenreView

from films_dict.views import MovieCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloView.as_view()),
    path('', MovieView.as_view(), name='index'),
    path('movie/create', MovieCreateView.as_view(success_url='create'), name='movie_create'),
    path('movie/update/<pk>', MovieUpdateView.as_view(success_url='create'), name='movie_update'),

]