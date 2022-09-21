from rest_framework.viewsets import ModelViewSet
from books.models import Author, Book
from books.serializers import AuthorSerializer, BookOutputSerializer, BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class AuthorViewSet(ModelViewSet):
    serializer_class =  AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]
    ordering_fields = ["first_name", "last_name"]
    
    
    
class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["author", "name"]
    search_fields = ["author", "name", "isbn"]
    ordering_fields = ["author", "name", "isbn"]
    
    def get_serializer_class(self):
        
        if self.action in ["list", "retrieve"]:
            return BookOutputSerializer
        return super().get_serializer_class()