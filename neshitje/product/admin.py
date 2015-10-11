from django.contrib import admin
from .models import Currency, Condition, Product, ProductImage
# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    class Meta:
        model = Currency

admin.site.register(Currency)

class ConditionAdmin(admin.ModelAdmin):
    class Meta:
        model = Condition

admin.site.register(Condition)

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

admin.site.register(Product)

class ProdcutImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductImage

admin.site.register(ProductImage)
