import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class SourceID(models.Model):
    source_name = models.CharField(max_length=60)
    http_ref = models.CharField(max_length=80, blank=True, null=True)
    date_added = models.DateTimeField("Date Created", null=True, auto_now_add=True, auto_now=False)
    status_changed = models.DateTimeField("Date Created", null=True, auto_now_add=False, auto_now=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.source_name


class CookieTracker(models.Model):
    source = models.ForeignKey(SourceID, default=1)
    date_added = models.DateTimeField("Date Created")

    def __str__(self):
        return str(self.id)


class SessionTracker(models.Model):
    source_id = models.ForeignKey(SourceID, default=1)
    ref_url = models.CharField(max_length=1024)
    session_start = models.DateTimeField("Date time created")
    ip_v4 = models.CharField(max_length=14)
    ip_v6 = models.CharField(max_length=46)
    user_agent = models.CharField(max_length=1024)
    country_code = models.CharField(max_length=3)
    city = models.CharField(max_length=25)
    cookie = models.ForeignKey(CookieTracker)
    mktg_trck_id = models.CharField(max_length=20)
    language_code = models.CharField(max_length=3)
    session_owner = models.IntegerField(User, blank=True, null=True)

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
