from django.contrib import admin

# Register your models here.

from .models import Genre, Book

admin.site.register(Genre)
admin.site.register(Book)