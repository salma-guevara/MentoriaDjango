
from email.policy import default
from re import VERBOSE
from tabnanny import verbose
from django.db import models

# Create your models here.
class Author(models.Model): #Tabla padre
      first_name = models.CharField(max_length=120, verbose_name='Nombre')
      last_name = models.CharField(max_length=120, verbose_name='Apellido')
      birth_date = models.DateField(verbose_name='Fecha de nacimiento')
      created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
      status = models.BooleanField(default=True, verbose_name='Status')
      
      class Meta:
          db_table = 'authors'
          

class Book(models.Model): #Tabla hijo
    name = models.CharField(max_length=128, verbose_name='Nombre del libro') #El verbosename es una recomendación de Rob.
    isbn = models.IntegerField(default=0,verbose_name='ISBN del libro')
    publisher_date = models.DateField(verbose_name='Fecha de publicación')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True, verbose_name='relación a clase Author')
    
    class Meta:
        db_table = 'books'  #Esto nos servirá para agregarle un nombre a la tabla y no se ponga uno por default


