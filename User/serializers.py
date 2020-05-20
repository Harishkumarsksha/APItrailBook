from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book,Author,Publications
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    publications = serializers.StringRelatedField(many=True)
    class Meta:
        model = Author 
        fields = ('name','email','phone_no','book','publications')

class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'

