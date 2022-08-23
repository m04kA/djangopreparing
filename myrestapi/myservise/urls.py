from django.urls import path, include
from .views import BooksViewSet, AuthorsViewSet, GenresViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'books', BooksViewSet)

routers.register(r'authors', AuthorsViewSet)

routers.register(r'genres', GenresViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]
