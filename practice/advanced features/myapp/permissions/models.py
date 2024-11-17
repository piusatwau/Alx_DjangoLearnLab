from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    
    class Meta:
        permissions = [
            ('can_approve','can approve new posts'),
            ('can_rename', 'can rename old posts'),            
        ]
        
    def __str__(self):
        return f'{self.name}'
