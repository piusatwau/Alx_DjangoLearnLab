from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

ORDER_STATUS = (
    ('Pending', 'Pending'),
    ('Comfirmed', 'Comfirmed'),
    ('Shipped', 'Shipped'),
    ('Cancelled', 'Cancelled'),
    ('Delivered', 'Delivered'),
)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='orders')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    created_on = models.DateTimeField(auto_now=True)
    update_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='Pending')
    