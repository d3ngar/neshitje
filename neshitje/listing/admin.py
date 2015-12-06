from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from .models import Currency, Listing, ListingImage, CategoryTree, Attribute, AttributeChoices, AttributeMapping
# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    class Meta:
        model = Currency

admin.site.register(Currency)

class ListingAdmin(admin.ModelAdmin):
    class Meta:
        model = Listing

admin.site.register(Listing)

class ListingImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ListingImage

admin.site.register(ListingImage)

class AttributeAdmin(admin.ModelAdmin):
    class Meta:
        model = Attribute

admin.site.register(Attribute)

class AttributeChoicesAdmin(admin.ModelAdmin):
    class Meta:
        model = AttributeChoices

admin.site.register(AttributeChoices)

class AttributeMappingAdmin(admin.ModelAdmin):
    class Meta:
        model = AttributeMapping

admin.site.register(AttributeMapping)



class CategoryTreeAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('category_name',)

    # Specify name of sortable property
    sortable = 'custom_order'

admin.site.register(CategoryTree, CategoryTreeAdmin)
