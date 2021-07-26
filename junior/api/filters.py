from django_filters import rest_framework as filters

from . import models


class BookFilter(filters.FilterSet):

    class Meta:
        model = models.Book
        fields = {
            "name": ['istartswith', 'iendswith']
        }