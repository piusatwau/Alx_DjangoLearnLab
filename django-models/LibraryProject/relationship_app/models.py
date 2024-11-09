from django.db import models

# Create your models here.

# Author model

class Author(models.Model):
    name =models.CharField(max_length=200)
    

# Book Model
class Book(models.Model):
    title=models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
# Library Model

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)
    

# Librarian Models

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
