from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  path('getbooks', views.get_books),
  path('addbook', views.add_book),
]