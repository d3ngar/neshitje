import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from main_app.models import Status

# Create your models here.

class UserDetail(models.Model):
    date_created = models.DateTimeField("Date time created", auto_now_add=True, auto_now=False)
    status = models.ForeignKey(Status, default=1)
    status_changed = models.DateTimeField("Date time updated", auto_now_add=False, auto_now=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(User)
    marketing_optin = models.BooleanField(default=True)

    def __str__(self):
        return self.user


class UserBilling(models.Model):
    date_created = models.DateTimeField("Date time created", auto_now_add=True, auto_now=False)
    is_active = models.BooleanField(default=True)
    address_line_1 = models.CharField(max_length=55, blank=True, null=True)
    address_line_2 = models.CharField(max_length=55, blank=True, null=True)
    address_line_3 = models.CharField(max_length=55, blank=True, null=True)
    city = models.CharField(max_length=55, blank=True, null=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    user = models.ForeignKey(User)
    status_changed = models.DateTimeField("Date time updated", auto_now_add=False, auto_now=True)
    status = models.ForeignKey(Status, default=1)

    def __str__(self):
        return str(self.address_line_1)


class UserShipping(models.Model):
    address_line_1 = models.CharField(max_length=55, blank=True, null=True)
    address_line_2 = models.CharField(max_length=55, blank=True, null=True)
    address_line_3 = models.CharField(max_length=55, blank=True, null=True)
    city = models.CharField(max_length=55, blank=True, null=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    address_nick = models.CharField(max_length=55, blank=True, null=True)
    date_created = models.DateTimeField("Date time created", auto_now_add=True, auto_now=False)
    is_active = models.BooleanField(default = True)
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status, default=1)
    status_changed = models.DateTimeField("Date time updated", auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.address_nick

# Other infos
