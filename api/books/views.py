from rest_framework import viewsets

from books.serializers import (
    AuthorSerializer, BookSerializer, CategorySerializer
)
from base.models import AuthorModel, BookModel, CategoryModel


class AuthorViewSet(viewsets.ModelViewSet):
    """Manage authors in the database"""
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Manage categories in the database"""
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class BooksList(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
