from rest_framework import serializers

from .models import Books, Authors, Genres


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    """
    Serializer for Books model.
    """
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Books
        exclude = ('created_at',)
        read_only_fields = ('created_at', 'updated_at')
