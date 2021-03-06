import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from main_app.models import Status


# Create your models here.

class SourceID(models.Model):
    source_name = models.CharField(max_length=60)
    http_ref = models.CharField(max_length=80, blank=True, null=True)
    date_added = models.DateTimeField("Date Created", null=True, auto_now_add=True, auto_now=False)
    status_changed = models.DateTimeField("Date Created", null=True, auto_now_add=False, auto_now=True)
    status = models.ForeignKey(Status, default=1)

    def __str__(self):
        return self.source_name


class CookieTracker(models.Model):
    source = models.ForeignKey(SourceID, default=1)
    date_added = models.DateTimeField("Date Created")

    def __str__(self):
        return str(self.id)


class SessionTracker(models.Model):
    source_id = models.ForeignKey(SourceID, default=1)
    ref_url = models.CharField(max_length=1024, null=True, blank=True)
    session_start = models.DateTimeField("Date time created")
    ip_v4 = models.CharField(max_length=14)
    ip_v6 = models.CharField(max_length=46, blank=True, null=True)
    user_agent = models.CharField(max_length=1024, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    cookie = models.ForeignKey(CookieTracker)
    mktg_trck_id = models.CharField(max_length=20, blank=True, null=True)
    language_code = models.CharField(max_length=6)
    session_owner = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)


class PageTracker(models.Model):
    session = models.ForeignKey(SessionTracker)
    time_stamp = models.DateTimeField("Date time created")
    user_agent = models.CharField(max_length=1024)
    ip_v4 = models.CharField(max_length=14, blank=True, null=True)
    ip_v6 = models.CharField(max_length=46, blank=True, null=True)
    ref_url = models.CharField(max_length=1024, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    page_count = models.IntegerField(default=0)
    curr_url = models.CharField(max_length=200)
    language_code = models.CharField(max_length=5, default="en-gb")

    def __str__(self):
        return str(self.id)

class Bot(models.Model):
    ip_v4 = models.CharField(max_length=16, blank=True, null=True)
    ip_v6 = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.CharField(max_length=2050, blank=True, null=True)
