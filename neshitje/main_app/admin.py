from django.contrib import admin

# Register your models here.
from .models import Status

class StatusAdmin(admin.ModelAdmin):
    class Meta:
        model = Status

admin.site.register(Status)
