from django import forms
from django.core.exceptions import ValidationError
from django.forms import SelectDateWidget
from films_dict.models import Genre, Movie, Director, Country
import re
from datetime import date


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


def validate_len_name(value):
    if len(value) > 25:
        raise ValidationError('So long film title')


class PastMonthField(forms.DateField):
    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

    title = forms.CharField(max_length=100, validators=[capitalized_validator, validate_len_name])
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    rating = forms.IntegerField(min_value=1, max_value=10)
    released = PastMonthField()
    description = forms.CharField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
                                  required=False)
    director = forms.ModelChoiceField(queryset=Director.objects.all())

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        cleaned = '.'.join(sentence.capitalize() for sentence in sentences)
        return cleaned

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'comedy' and result['rating'] > 5:
            raise ValidationError('The best comedy is worth a 4.')
        return result
