from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    KIDS = '1'
    TEENS = '2'
    ADULTS = '3'
    AGE_LIMIT_CHOICES = (
       (KIDS, 'Kids'),
       (TEENS, 'Teens'),
       (ADULTS, 'Adults')
    )
    age_limit = models.CharField(max_length=2, choices=AGE_LIMIT_CHOICES)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('first_name', 'second_name')

    def __str__(self):
        return f"{self.first_name} from {self.second_name}"


class Country(models.Model):
    countries_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.countries_name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.DO_NOTHING)
    director = models.ForeignKey(Director, null=True, on_delete=models.DO_NOTHING)
    countries = models.ManyToManyField(Country, related_name="movies")

    class Meta:
        unique_together = ('title', 'released')

    def __str__(self):
        return f"{self.title} from {self.released}"






