from rest_framework.serializers import ModelSerializer
from books.models import Book, Author

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookOutputSerializer(ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model  = Book
        fields = "__all__"
        
        
class BookSerializer(ModelSerializer):
    class Meta:
        model  = Book
        fields = "__all__"