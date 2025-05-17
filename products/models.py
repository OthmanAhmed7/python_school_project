from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    ex_date = models.DateField()
    country = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.CharField(choices=[('milk', 'milk'), ('chips', 'chips'), ('candy', 'candy')], max_length=10)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name