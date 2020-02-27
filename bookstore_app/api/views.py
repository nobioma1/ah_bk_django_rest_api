from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookSerializer
from .models import Book, Author
from rest_framework import status
import json
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def welcome(request):
  content = { 'message': 'Welcome AH_Bookstore App!' }
  return JsonResponse(content, status=200)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_books(request):
  user = request.user.id
  books = Book.objects.filter(added_by=user)
  serializer = BookSerializer(books, many=True)
  return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_book(request):
  payload = json.loads(request.body)
  user = request.user
  author = Author.objects.get(id=payload["author"])
  book = Book.objects.create(
    title = payload["title"],
    description = payload["description"],
    added_by = user,
    author = author
  )
  serializer = BookSerializer(book)
  return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)

