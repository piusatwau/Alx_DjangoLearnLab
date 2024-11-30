from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group

# User manager

class UserManger(BaseUserManager):
    
    
    def create_user(self, email, password):
        if not email:
            raise ValueError('Email is required')
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password):
        user =self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



# Custom user model

class User(AbstractUser):
      
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=False, max_length=10)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []
    objects = UserManger
    
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Ensure unique related name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Ensure unique related name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    
  
    
    
    
