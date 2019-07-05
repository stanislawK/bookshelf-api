from rest_framework import status
import pytest

from base.models import BookModel
from books.serializers import BookSerializer

BOOKS_URL = '/api/book/books/'


@pytest.mark.django_db
class TestBook():
    """Tests for book object"""
    def test_serialize_valid_book(self, author, book, category):
        serializer = BookSerializer(book)

        assert serializer.data['title'] == book.title
        assert serializer.data['authors'][0] == author.name
        assert serializer.data['categories'][0] == category.name

    def test_retrive_books(self, book, client):
        """Test retrive books list"""
        response = client.get(BOOKS_URL)
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data == serializer.data
