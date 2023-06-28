from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _


# Product model
class Product(models.Model):
    name = models.CharField(_("name"), max_length=120)
    subtitle = models.TextField(_("subtitle"), max_length=500)
    description = models.TextField(_("description"), max_length=50000)
    price = models.FloatField(_("price"))
    quantity = models.IntegerField(_("quantity"))
    sku = models.IntegerField(_("sku"))
    brand = models.ForeignKey('Brand', verbose_name=_("brand"), related_name="products_brand", on_delete=models.SET_NULL, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name
    

# Product Images model
class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"), related_name="product_image", on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to="product_images")

    def __str__(self):
        return str(self.product)


# Brand model
class Brand(models.Model):
    name = models.CharField(_("name"), max_length=100)
    image = models.ImageField(_("image"), upload_to='brands')

    def __str__(self):
        return self.name


# Review model
class Review(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), related_name="review_author", on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name=_("product"), related_name="product_review", on_delete=models.CASCADE)
    review = models.TextField(_("review"), max_length=500)
    rate = models.IntegerField(_("rate"), )
    create_date = models.DateTimeField(_("create_date"), default=timezone.now)

    def __str__(self):
        return str(self.product)