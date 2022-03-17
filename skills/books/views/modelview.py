from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    permissions_classes = (AllowAny, )
    serializer_class = AuthorSerializer
    
    
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permissions_classes = (AllowAny, )
    serializer_class = BookSerializer