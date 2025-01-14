from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title