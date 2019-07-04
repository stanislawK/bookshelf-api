import pytest

from books.serializers import BookSerializer


@pytest.mark.django_db
class TestBook():
    """Tests for book object"""
    def test_serialize_valid_book(self, author, book, category):
        serializer = BookSerializer(book)

        assert serializer.data['title'] == book.title
        assert serializer.data['authors'][0] == author.name
        assert serializer.data['categories'][0] == category.name
