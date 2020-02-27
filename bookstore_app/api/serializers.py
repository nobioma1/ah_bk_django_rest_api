from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['id', 'name', 'added_by', 'created_date']

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['id', 'title', 'description', 'author', 'added_by', 'created_date']