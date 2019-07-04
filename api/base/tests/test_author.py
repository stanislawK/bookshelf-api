import pytest

from books.serializers import AuthorSerializer


@pytest.mark.django_db
class TestAuthor():
    """Tests for author serializer"""
    def test_serialize_valid_author(self, author):
        serializer = AuthorSerializer(author)

        assert serializer.data['name'] == author.name

    def test_serialize_invalid_authors_data(self):
        long_name = 'a' * 256
        author = {'name': long_name}
        serializer = AuthorSerializer(data=author)

        assert not serializer.is_valid()
        assert 'no more than 255 characters' in serializer.errors['name'][0]
