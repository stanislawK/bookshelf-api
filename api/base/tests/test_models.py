import pytest
from base.models import AuthorModel


@pytest.mark.django_db
class TestModels():
    """Tests for author model"""
    def test_new_author(self):
        """Test creating a new author"""
        author = AuthorModel.objects.create(name='Tolkien')
        authors_db = AuthorModel.objects.all()

        assert str(author) == author.name
        assert authors_db[0] == author
