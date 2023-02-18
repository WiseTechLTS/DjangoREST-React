from django.db import models
from authentication.models import User
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    
    def __str__(self):
        return self.user.username