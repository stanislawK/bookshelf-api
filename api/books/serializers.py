from rest_framework import serializers

from base.models import AuthorModel, CategoryModel


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for author object"""

    class Meta:
        model = AuthorModel
        fields = ('id', 'name')
        read_only_fields = ('id',)


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category object"""

    class Meta:
        model = CategoryModel
        fields = ('id', 'name')
        read_only_fields = ('id',)
