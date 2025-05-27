from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    phone=models.CharField(max_length=11)
    gender=models.CharField(choices=[('male', 'male'), ('female', 'female')])

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    ex_date = models.DateField()
    country = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.CharField(choices=[('laptop', 'laptop'), ('pc', 'pc'), ('phones', 'phones')], max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)