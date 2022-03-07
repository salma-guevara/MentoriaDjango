from django.shortcuts import get_object_or_404 #Nos regresará un error 404 *

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from books.models import Book, Author


from books.serializers import AuthorSerializer, BookSerializer

# Create your views here.
class RetrieveBooks(APIView):
    permissions_classes = (AllowAny,)
    
    def get(self,request):
        books_list = Book.objects.all()
        serializer = BookSerializer(books_list,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RetrieveAuthors(APIView):
    permissions_classes = (AllowAny,)
    
    def get(self,request):
        author_list = Author.objects.all()
        serializer = AuthorSerializer(author_list, many=True) #con el último parámetro, le indicamos al serializador que hay más de un objeto en esa lista
        return Response(serializer.data) #Toma los datos y los convierte a formato json.
    
    
class CreateAuthor(APIView): #Con este apartado pudimos meter información en nuestro servidor
    permissions_classes = (AllowAny,)
    
    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data = data)
        serializer.is_valid(raise_exception=True) #toma el serializador y valida que los datos en data sean correctos y sean acordes a lo que pedimos en nuestro modelo
        serializer.save() # guarda los datos y los envía directo a la BD
        return Response(serializer.data, status=status.HTTP_201_CREATED) #Le indico al navegador y al frontend que el registro ha sido creado
    
    
class CreateBook(APIView):
    permissions_classes = (AllowAny,)
    
    def post(self, request):
        #Para no estar guardando variables de una sola vez, otra opción es:
        serializer = BookSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class RetriveAuthorAPIView(APIView):
    permissions_classes = (AllowAny,)
    
    def get(self,request,author_id):
        author_obj = Author.objects.get(id=author_id) #Aquí solo nos regresará el objeto que coinicida con los parámetros que le estamos pidiendo
        serializer = AuthorSerializer(author_obj) #aqui el many=True no es necesario porque solo nos va a devolver un objeto
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class RetriveBookAPIView(APIView):
    permissions_classes = (AllowAny,)
    
    def get(self,request,book_id):
        book_obj = get_object_or_404(Book, pk=book_id) #* 
        serializer = BookSerializer(book_obj) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)