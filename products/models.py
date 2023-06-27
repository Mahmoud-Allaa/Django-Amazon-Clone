from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=50000)
    price = models.FloatField()
    quantity = models.IntegerField()
    sku = models.IntegerField()
    brand = models.ForeignKey('Brand', related_name="product_brand", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brands')

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, related_name="review_author", on_delete=models.SET_NULL, null=True, blank=True)
    Product = models.ForeignKey(Product, related_name="product_review", on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now)