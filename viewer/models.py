from django.db import models
from django.utils.text import slugify

# Create your models here.
from django.db.models import CharField, Model, ForeignKey, DO_NOTHING, IntegerField, DateField, TextField, \
    DateTimeField, SlugField


class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birth_date = models.DateField()
    EYE_COLOR_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('hazel', 'Hazel'),
        ('dark', 'Dark'),
    ]
    eye_color = models.CharField(max_length=5, choices=EYE_COLOR_CHOICES)

    def __str__(self):
        return self.name

class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
    slug = SlugField(unique=True, editable=False)
    actors = models.ManyToManyField(Actor, related_name='movies')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


