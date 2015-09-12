import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class user_details(models.Model):
    date_created = models.DateTimeField("Date time created")
    is_active = models.BooleanField(default=True)
    status_changed = models.DateTimeField("Date time updated")
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user


class user_billing(models.Model):
    date_created = models.DateTimeField("Date time created")
    is_active = models.BooleanField(default=True)
    address_line_1 = models.CharField(max_length=55, blank=True, null=True)
    address_line_2 = models.CharField(max_length=55, blank=True, null=True)
    address_line_3 = models.CharField(max_length=55, blank=True, null=True)
    city = models.CharField(max_length=55, blank=True, null=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    user = models.ForeignKey(User)
    status_changed = models.DateTimeField("Date time updated")

    def __str__(self):
        return self.address_line_1 + "|" + self.address_line_2  + "|" +  self.post_code + "|" + self.city


class user_shipping_address(models.Model):
    address_line_1 = models.CharField(max_length=55, blank=True, null=True)
    address_line_2 = models.CharField(max_length=55, blank=True, null=True)
    address_line_3 = models.CharField(max_length=55, blank=True, null=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    address_nick = models.CharField(max_length=55, blank=True, null=True)
    date_created = models.DateTimeField("Date time created")
    is_active = models.BooleanField(default = True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.address_nick
