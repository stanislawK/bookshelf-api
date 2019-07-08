from django.urls import reverse
from rest_framework import status
import pytest

from base.models import AuthorModel, BookModel, CategoryModel
from books.serializers import BookSerializer

BOOKS_URL = reverse('book:bookmodel-list')


def detail_url(book_id):
    return reverse('book:bookmodel-detail', args=[book_id])


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

    def test_view_book_detail(self, book, client):
        """Test retrieve book detail"""
        response = client.get(detail_url(book.id))
        serializer = BookSerializer(book)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_create_book(self, book_payload, client):
        """Test create new book"""
        response = client.post(BOOKS_URL, book_payload)

        book = BookModel.objects.all()[0]

        assert response.status_code == status.HTTP_201_CREATED
        for key in book_payload.keys():
            assert book_payload[key] == getattr(book, key)

    def test_create_book_with_author(self, author, book_payload, client):
        book_payload['authors'] = author.name

        response = client.post(BOOKS_URL, book_payload)

        book = BookModel.objects.all()[0]

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == book.title
        assert response.data['authors'][0] == author.name

    def test_create_book_with_authors(self, book_payload, client):
        book_payload['authors'] = ['Tolkien', 'Okken']

        response = client.post(BOOKS_URL, book_payload)

        book = BookModel.objects.all().last()
        authors = AuthorModel.objects.all()

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == book.title
        for author in book_payload['authors']:
            assert author in [el.name for el in book.authors.all()]
            assert authors.get(name=author)

    def test_create_book_with_category(self, book_payload, category, client):
        book_payload['categories'] = category.name

        response = client.post(BOOKS_URL, book_payload)

        book = BookModel.objects.all()[0]

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == book.title
        assert category.name in response.data['categories']

    def test_create_book_with_categories(self, book_payload, client):
        book_payload['categories'] = ['Fantasy', 'Historic']

        response = client.post(BOOKS_URL, book_payload)

        book = BookModel.objects.all().last()
        categories = CategoryModel.objects.all()

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == book.title
        for category in book_payload['categories']:
            assert category in [el.name for el in book.categories.all()]
            assert categories.get(name=category)

    def test_create_complete_book(self, book_payload, client):
        book_payload['authors'] = ['Tolkien', 'Okken']
        book_payload['categories'] = ['Fantasy', 'Historic']

        response = client.post(BOOKS_URL, book_payload)

        authors = AuthorModel.objects.all()
        book = BookModel.objects.all().last()
        categories = CategoryModel.objects.all()

        assert response.status_code == status.HTTP_201_CREATED
        for author in book_payload['authors']:
            assert author in [el.name for el in book.authors.all()]
            assert authors.get(name=author)
        for category in book_payload['categories']:
            assert category in [el.name for el in book.categories.all()]
            assert categories.get(name=category)
