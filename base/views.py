from django.shortcuts import render, get_object_or_404

# Create your views here.

from rest_framework import viewsets
from .models import Genre, Book
from .serializers.genre_serializer import GenreSerializer
from .serializers.book_serializer import BookSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def genres(request):
    genres = Genre.objects.all()
    return render(request, 'base/genres.html', {'genres': genres})

def books(request):
    books = Book.objects.all()
    return render(request, 'base/books.html', {'books': books})

def genre_books(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    books = Book.objects.filter(genre=genre)
    return render(request, 'base/genre_books.html', {'genre': genre, 'books': books})

def home(request):
    books = Book.objects.all()[:6]
    return render(request, 'base/home.html', {'books': books})