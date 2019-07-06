from django.urls import reverse
from rest_framework import status
import pytest

from base.models import AuthorModel
from books.serializers import AuthorSerializer


AUTHORS_URL = reverse('book:authormodel-list')


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

    def test_retrive_authors(self, author, client):
        response = client.get(AUTHORS_URL)
        authors = AuthorModel.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_create_author_invalid(self, client):
        payload = {'name': ''}
        response = client.post(AUTHORS_URL, payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_author_successful(self, client):
        payload = {'name': 'Okken'}
        response = client.post(AUTHORS_URL, payload)
        exists = AuthorModel.objects.filter(name=payload['name']).exists()

        assert response.status_code == status.HTTP_201_CREATED
        assert exists
