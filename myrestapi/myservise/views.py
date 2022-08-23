from rest_framework import viewsets, filters
from .serializers import BooksSerializer, AuthorsSerializer, GenresSerializer
from .models import Books, Authors, Genres


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'published']
    ordering = ['-price']


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['first_name', 'last_name']
    ordering = ['-first_name']


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']
    ordering = ['-name']
