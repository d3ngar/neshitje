from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from .models import Currency, Condition, Listing, ListingImage, CategoryTree
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


class CategoryTreeAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('category_name',)

    # Specify name of sortable property
    sortable = 'custom_order'

admin.site.register(CategoryTree, CategoryTreeAdmin)
