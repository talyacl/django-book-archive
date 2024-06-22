from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
