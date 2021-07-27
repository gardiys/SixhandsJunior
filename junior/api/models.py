from django.db import models


from django.contrib.auth.models import AbstractUser


class UserRole(models.IntegerChoices):
    USER = 1
    ADMIN = 2
    MANAGER = 3


class BookCover(models.IntegerChoices):
    HARD = 1
    SOFT = 2


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=UserRole.choices, default=UserRole.USER)


class Author(models.Model):
    name = models.CharField(max_length=255)


class Shelf(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    name = models.CharField(max_length=127)
    pages = models.PositiveIntegerField()
    cover = models.PositiveSmallIntegerField(choices=BookCover.choices)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, null=True, default=None, blank=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name
