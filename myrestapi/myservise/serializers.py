from rest_framework import serializers

from .models import Books


class BooksSerializer(serializers.ModelSerializer):
    """
    Serializer for Books model.
    """
    class Meta:
        model = Books
        fields = "__all__"
        read_only_fields = ('created_at', 'updated_at')
