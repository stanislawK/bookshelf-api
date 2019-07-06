import os
import django
from django.conf import settings
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')


def pytest_configure():
    settings.DEBUG = False
    django.setup()


@pytest.fixture
def author():
    from base.models import AuthorModel
    return AuthorModel.objects.create(name='Tolkien')


@pytest.fixture
def category():
    from base.models import CategoryModel
    return CategoryModel.objects.create(name="Fiction")


@pytest.fixture
def book(author, category):
    from base.models import BookModel
    book = BookModel.objects.create(
        title='Hobbit',
        description='Book about hobbits'
    )
    book.authors.add(author)
    book.categories.add(category)
    return book


@pytest.fixture
def client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def book_payload(book):
    payload = {
        'title': book.title,
        'description': book.description,
    }
    return payload
