from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="photo%y%m%d")
    active = models.BooleanField(default=True)
