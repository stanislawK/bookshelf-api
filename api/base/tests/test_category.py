from django.urls import reverse
from rest_framework import status
import pytest

from base.models import CategoryModel
from books.serializers import CategorySerializer


CATEGORIES_URL = reverse('book:categorymodel-list')


@pytest.mark.django_db
class TestCategory():
    """Tests for title object"""
    def test_serialize_valid_title(self, category):
        serializer = CategorySerializer(category)

        assert serializer.data['name'] == category.name

    def test_serialize_invalid_category_data(self):
        long_name = 'a' * 256
        category = {'name': long_name}
        serializer = CategorySerializer(data=category)

        assert not serializer.is_valid()
        assert 'no more than 255 characters' in serializer.errors['name'][0]

    def test_retrieve_categories(self, category, client):
        response = client.get(CATEGORIES_URL)
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_create_category_successful(self, client):
        payload = {'name': 'Fantasy'}
        response = client.post(CATEGORIES_URL, payload)
        exists = CategoryModel.objects.filter(name=payload['name']).exists()

        assert response.status_code == status.HTTP_201_CREATED
        assert exists

    def test_create_category_invalid(self, client):
        payload = {'name': ''}
        response = client.post(CATEGORIES_URL, payload)
        categories = CategoryModel.objects.all()

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not categories
