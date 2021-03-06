from django.contrib import admin
from .models import Currency, Condition, Listing, ListingImage
# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    class Meta:
        model = Currency

admin.site.register(Currency)

class ConditionAdmin(admin.ModelAdmin):
    class Meta:
        model = Condition

admin.site.register(Condition)

class ListingAdmin(admin.ModelAdmin):
    class Meta:
        model = Listing

admin.site.register(Listing)

class ListingImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ListingImage

admin.site.register(ListingImage)
