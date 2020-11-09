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
from django.urls import path, include


from films_dict.views import hello

from django_movies.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', IndexView.as_view(), name='index'),
    path('films_dict/', include('films_dict.urls', namespace='films_dict')),
    path('accounts/', include('accounts.urls', namespace='accounts')),

]
