from rest_framework import serializers

from . import models


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = "__all__"
