from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters
from .serializers import BooksSerializer
from myrestapi.myservise.models import Books


class HelloWorld(APIView):
    def get(self, request):
        return Response({'message': 'Hello World!'}, status=200)


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('price', 'published')
    ordering = ('-price',)
