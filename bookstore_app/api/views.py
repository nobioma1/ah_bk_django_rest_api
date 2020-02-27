from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def welcome(request):
  content = { 'message': 'Welcome AH_Bookstore App!' }
  return JsonResponse(content, status=200)

