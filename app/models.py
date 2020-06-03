from django.db import models
from decimal import Decimal

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default='')
    desc=models.CharField(max_length=300)
    price=models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00))
    image=models.ImageField(upload_to='shop/images', default='')
    def __str__(self):
        return self.product_name

class User(models.Model):
    user_id=models.AutoField
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    city=models.CharField(max_length=10)
    country=models.CharField(max_length=10)
    password=models.CharField(max_length=16)
    def __str__(self):
        return str(self.id) +". "+ self.fname +" "+ self.lname
