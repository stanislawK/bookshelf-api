from rest_framework import status, viewsets
from rest_framework.response import Response

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

    def create(self, request):
        authors = request.data.getlist('authors')
        categories = request.data.getlist('categories')

        if authors:
            for i, name in enumerate(authors):
                author = add_author(name)
                request.data.getlist('authors')[i] = author

        if categories:
            for i, name in enumerate(categories):
                category = add_category(name)
                request.data.getlist('categories')[i] = category

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


def add_author(_name):
    if not AuthorModel.objects.filter(name=_name):
        author = AuthorSerializer(data={'name': _name})
        author.is_valid(raise_exception=True)
        author.save()
    return AuthorModel.objects.get(name=_name)


def add_category(_name):
    if not CategoryModel.objects.filter(name=_name):
        category = CategorySerializer(data={'name': _name})
        category.is_valid(raise_exception=True)
        category.save()
    return CategoryModel.objects.get(name=_name)
