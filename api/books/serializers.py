from rest_framework import status
from rest_framework import serializers

from base.models import AuthorModel, CategoryModel, BookModel


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


class BookSerializer(serializers.ModelSerializer):
    """Serializer for book object"""
    authors = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=AuthorModel.objects.all()
    )
    categories = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=CategoryModel.objects.all()
    )

    class Meta:
        model = BookModel
        fields = ('id', 'title', 'description', 'authors', 'categories')
        read_only_fields = ('id',)
