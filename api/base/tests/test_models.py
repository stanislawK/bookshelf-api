import pytest
from base.models import AuthorModel, BookModel, CategoryModel


@pytest.mark.django_db
class TestModels():
    """Tests for author model"""
    def test_new_author(self):
        """Test creating a new author"""
        author = AuthorModel.objects.create(name='Tolkien')
        authors_db = AuthorModel.objects.all()

        assert str(author) == author.name
        assert authors_db[0] == author

    def test_new_category(self):
        """Test creating a new category"""
        category = CategoryModel.objects.create(name="Fiction")
        category_db = CategoryModel.objects.all()

        assert str(category) == category.name
        assert category_db[0] == category

    def test_new_book(self, author, category):
        """Test creating new book"""
        book = BookModel.objects.create(
            title="Lord of the rings",
            description="Lorem ipsum",
        )
        book.authors.add(author)
        book.categories.add(category)
        book_db = BookModel.objects.all()

        assert str(book) == book.title
        assert book_db[0] == book
        assert book_db[0].authors.all()[0] == author
        assert book_db[0].categories.all()[0] == category
