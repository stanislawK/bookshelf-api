from rest_framework import viewsets

from books.serializers import AuthorSerializer, BookSerializer
from base.models import AuthorModel, BookModel


class AuthorViewSet(viewsets.ModelViewSet):
    """Manage authors in the database"""
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class BooksList(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
