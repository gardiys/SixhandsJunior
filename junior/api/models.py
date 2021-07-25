from django.db import models


# Create your models here.
class BookCover(models.IntegerChoices):
    HARD = 1
    SOFT = 2


class Author(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    name = models.CharField(max_length=127)
    pages = models.PositiveIntegerField()
    cover = models.PositiveSmallIntegerField(choices=BookCover.choices)
    authors = models.ManyToManyField(Author)
