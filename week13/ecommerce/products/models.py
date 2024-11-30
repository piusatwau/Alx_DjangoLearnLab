from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# CATEGORY_CHOICES = (
#     ('CLOTHES', 'CLOTHES'),
#     ('ELECTRONICS', 'ELECTRONICS'),
#     ('DEVICES', 'DEVICES'),
# )
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category =models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products", default=None, null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)
    
