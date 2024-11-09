from django.db import models

# Create your models here.

# Author model

class Author(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

# Book Model
class Book(models.Model):
    title=models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.name
    
# Library Model

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name ='libraries')
    
    def __str__(self):
        return self.name
    

# Librarian Models

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    
    def __str__(self):
        return self.name
