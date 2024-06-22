# library/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'genres', views.GenreViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path ('', views.home, name='home'),
    path('genres/', views.genres, name='genres'),
    path('books/', views.books, name='books'),
    path('genres/<int:genre_id>/', views.genre_books, name='genre_books'),
    ]

urlpatterns += router.urls
