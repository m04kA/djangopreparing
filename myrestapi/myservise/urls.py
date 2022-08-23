from django.urls import path, include

from . import views
from .views import BooksViewSet, AuthorsViewSet, GenresViewSet
from rest_framework import routers

routers_book = routers.DefaultRouter()
routers_book.register(r'books', BooksViewSet)

routers_author = routers.DefaultRouter()
routers_author.register(r'authors', AuthorsViewSet)

routers_genre = routers.DefaultRouter()
routers_genre.register(r'genres', GenresViewSet)




urlpatterns = [
    path('hi/', views.HelloWorld.as_view()),
    path('', include(routers_book.urls)),
    path('', include(routers_author.urls)),
    path('', include(routers_genre.urls)),
]
