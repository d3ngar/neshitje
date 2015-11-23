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
from mptt.models import MPTTModel, TreeForeignKey

#fs = FileSystemStorage(location='media/photos')
# Create your models here.

def where_to_upload(instance, filename):
    listing = instance.listing.id
    user = instance.user.id
    filename = 'listing_images/' + str(user)  + "/" + str(product) + "/" + hashlib.md5(filename).hexdigest()+'.jpg'
    print "Created a unique filename: " + filename
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


class Listing(models.Model):
    listing_name = models.CharField(max_length=100)
    supplier_id = models.CharField(max_length=75, null=True, blank=True)
    listing_description = models.TextField()
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
        return self.listing_name


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing)
    status = models.ForeignKey(Status, default=1)
    user = models.ForeignKey(User)
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
        super(ListingImage, self).save()

    def __str__(self):
        return self.image


class CategoryTree(MPTTModel):
    category_name = models.CharField(max_length=100, unique=True)
    custom_order = models.PositiveIntegerField(default=1)
    parent = TreeForeignKey('self', null=True, blank=True, related_name="sub_category", db_index=True)

    class MPTTMeta:
        order_insertion_by = ['custom_order']

    def save(self, *args, **kwargs):
        super(CategoryTree, self).save(*args, **kwargs)
        CategoryTree.objects.rebuild()

    def __str__(self):
        return self.category_name


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=100)
    attribute_type = models.CharField(max_length=100)

    def __str__(self):
        return self.attribute_name


class AttributeChoices(models.Model):
    attribute = models.ForeignKey(Attribute)
    choice = models.CharField(max_length=100)
    choice_numer = models.IntegerField(null=True)

    def __str__(self):
        return self.choice

class AttributeMapping(models.Model):
    attribute = models.ForeignKey(Attribute)
    category = models.ForeignKey(CategoryTree)


"""


class ProductAttributeMapping(models.Model):
    #still to come

class CategoryTree(models.Model):
    #still to come
    product_mapping = models.BooleanField(default=True)


class ProductDeliveryMapping(models.Model):
    #still to come
"""
