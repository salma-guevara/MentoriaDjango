from rest_framework import serializers

from books.models import Author, Book  #Estamos llamando a los modelos de la sesión previa

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__' #Va a ir al modelo Author y va a traer todos los campos que tenga específicados + el id
        #fields = ('id','first_name','last_name','birth_date') #Si solo queremos ver campos específicos. Si después estamos agregando datos y no está el campo aquí, regresará un error.
        

class BookSerializer (serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
    def to_representation (self, instance):
        response = super().to_representation(instance)
        response['author'] = AuthorSerializer(instance.author).data
        return response