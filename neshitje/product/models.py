import datetime
import hashlib
import StringIO
from decimal import Decimal
from PIL import Image as Img
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from sorl.thumbnail import ImageField, get_thumbnail
from main_app.models import Status

#fs = FileSystemStorage(location='media/photos')
# Create your models here.

def where_to_upload(instance, filename):
    product = instance.product.id
    user = instance.user.id
    filename = 'product_images/' + str(user)  + "/" + str(product) + "/" + hashlib.md5(filename).hexdigest()+'.jpg'
    #print "Created a unique filename: " + filename
    return filename


class Currency(models.Model):
    currency_code = models.CharField(max_length=3)
    currency_symbol = models.CharField(max_length=5)
    currency_name = models.CharField(max_length=20)

    def __str__(self):
        return self.currency_code

class Condition(models.Model):
    condition_description = models.CharField(max_length=20)

    def __str__(self):
        return self.condition_description


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    supplier_id = models.CharField(max_length=75, null=True, blank=True)
    product_description = models.TextField()
    price = models.DecimalField (max_digits=20, decimal_places=4, default=Decimal('0.0000'))
    status = models.ForeignKey(Status, default=1)
    in_stock = models.IntegerField(default=1)
    user = models.ForeignKey(User)
    keywords = models.CharField(max_length=4000, null=True, blank=True)
    condition = models.ForeignKey(Condition)
    date_added = models.DateTimeField("Date Created", null=True, auto_now_add=True, auto_now=False)
    status_changed = models.DateTimeField("Date Created", null=True, auto_now_add=False, auto_now=True)
    currency_code = models.ForeignKey(Currency)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status, default=1)
    date_added = models.DateTimeField("Date Created", null=True, auto_now_add=True, auto_now=False)
    status_changed = models.DateTimeField("Date Created", null=True, auto_now_add=False, auto_now=True)
    image = models.ImageField(upload_to=where_to_upload)

    def save(self):
        if self.image:
            image = Img.open(StringIO.StringIO(self.image.read()))
            image.thumbnail((1920,1080), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=85)
            output.seek(0)
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name, 'image/jpeg', output.len, None)
        super(ProductImage, self).save()

    def __str__(self):
        return self.image


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



class ProductDeliveryMapping(models.Model):
    #still to come
"""
