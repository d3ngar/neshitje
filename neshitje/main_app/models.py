from django.db import models

# Create your models here.
class Status(models.Model):
    status_name = models.CharField(max_length="50")
    status_description = models.CharField(max_length="1000", blank=True, null=True)

    def __str__(self):
        return self.status_name
