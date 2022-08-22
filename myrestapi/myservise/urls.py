from django.urls import path, include

from . import views
from .views import BooksViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'books', BooksViewSet)


urlpatterns = [
    path('hi/', views.HelloWorld.as_view()),
    path('', include(routers.urls)),
]
