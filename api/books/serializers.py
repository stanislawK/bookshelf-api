from rest_framework import serializers

from base.models import AuthorModel


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for author object"""

    class Meta:
        model = AuthorModel
        fields = ('id', 'name')
        read_only_fields = ('id',)
