import pytest

from books.serializers import CategorySerializer


@pytest.mark.django_db
class TestCategory():
    """Test for Title object"""
    def test_serialize_valid_title(self, category):
        serializer = CategorySerializer(category)

        assert serializer.data['name'] == category.name

    def test_serialize_invalid_category_data(sel):
        long_name = 'a' * 256
        category = {'name': long_name}
        serializer = CategorySerializer(data=category)

        assert not serializer.is_valid()
        assert 'no more than 255 characters' in serializer.errors['name'][0]
