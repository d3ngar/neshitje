import datetime
from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    supplier_id = models.CharField(max_length=75)
    product_description = models.TextField()
    price = models.DecimalField (max_digits=20, decimal_places=4, default=Decimal('0.0000'))
    status = models.IntegerField(default=1)
    in_stock = models.IntegerField(default=1)
    user = models.ForeignKey(User)
    keywords = models.CharField(max_length=4000)
    condition = models.CharField(max_length=20)
    date_added = models.DateTimeField("Date Created", null=True, auto_now_add=True, auto_now=False)
    status_changed = models.DateTimeField("Date Created", null=True, auto_now_add=False, auto_now=True)


"""
class ProductAttribute(models.Model):
    #still to come

class ProductAttributeMapping(models.Model):
    #still to come

class CategoryTree(models.Model):
    #still to come
    product_mapping = models.BooleanField(default=True)

class CategoryTreeMapping(models.Model):
    #still to come

class ProductImages(models.Model):
    #still to come

class ProductDeliveryMapping(models.Model):
    #still to come
"""
