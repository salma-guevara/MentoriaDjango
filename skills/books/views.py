from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from books.models import Book, Author

# Create your views here.
class RetrieveBooks(APIView):
    permissions_classes = (AllowAny,)
    
    def get(self,request):
        books_list = Book.objects.all().values()
        return Response(books_list, status=status.HTTP_200_OK)
    

class RetrieveAuthors(APIView):
    permissions_classes = (AllowAny,)
    
    def get(self,request):
        author_list = Author.objects.all().values()
        return Response(author_list, status=status.HTTP_200_OK) #El status es información para el de front para que diga que tipo de info va a mostrar
    
    
class CreateAuthor(APIView): #Con este apartado pudimos meter información en nuestro servidor
    permissions_classes = (AllowAny,)
    
    def post(self, request):
        author_obj = Author.objects.create(
            first_name = request.data.get('first_name',''),
            last_name = request.data.get('last_name',''),
            birth_date = request.data.get('birth_date','')
        )
        return Response({'message':'Creado'}, status=status.HTTP_201_CREATED) #Le indico al navegador y al frontend que el registro ha sido creado
    
    
class CreateBook(APIView):
    permissions_classes = (AllowAny,)
    
    def post(self, request):
        book_obj = Book.objects.create(
            name = request.data.get('name',''),
            isbn = request.data.get('isbn',0),
            publisher_date = request.data.get('publisher_date','1700-01-01'),
            author_id = request.data.get('author_id',1)
        )
        return Response({'message':'Creado'}, status=status.HTTP_201_CREATED)