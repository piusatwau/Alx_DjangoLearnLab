from django.db import models

# Book model

class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f'{self.author} : {self.title}'