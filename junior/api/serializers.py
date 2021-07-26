from rest_framework import serializers

from . import models


class BookSerializer(serializers.ModelSerializer):
    some_data = serializers.SerializerMethodField(source='get_some_data')

    class Meta:
        model = models.Book
        fields = "__all__"

    def get_some_data(self, instance):
        return 1234


class BookSimpleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
