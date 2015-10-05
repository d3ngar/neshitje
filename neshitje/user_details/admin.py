from django.contrib import admin

# Register your models here.
from .models import UserDetail, UserBilling, UserShipping

class UserDetailAdmin(admin.ModelAdmin):
    class Meta:
        model = UserDetail

admin.site.register(UserDetail)


class UserBillingAdmin(admin.ModelAdmin):
    class Meta:
        model = UserBilling

admin.site.register(UserBilling)

class UserShippingAdmin(admin.ModelAdmin):
    class Meta:
        model = UserShipping

admin.site.register(UserShipping)
