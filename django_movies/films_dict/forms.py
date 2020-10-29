from django import forms
from django.forms import SelectDateWidget
from films_dict.models import Genre, Movie, Director, Country


class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    rating = forms.IntegerField(min_value=1, max_value=10)
    released = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
    description = forms.CharField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")), required=False)
    director = forms.ModelChoiceField(queryset=Director.objects.all())
    #countries = forms.ModelMultipleChoiceField(queryset=Country.objects.all())