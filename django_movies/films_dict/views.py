from django.shortcuts import render


# Create your views here.

def hello(request):
    return render(
        request,
        template_name="hello.html",
        context={'adjectives':['beautiful', 'cruel', 'wonderful']}
    )


def movies(request):
    return render(
        request,
        template_name="movies.html",
        context={'movies': Movie.objects.all()},
    )