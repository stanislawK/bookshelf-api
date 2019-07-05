from rest_framework import viewsets, mixins

from books.serializers import BookSerializer
from base.models import BookModel


class BooksList(viewsets.ModelViewSet, mixins.ListModelMixin):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
