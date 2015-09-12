from django.conf.urls import url, patterns, include

from . import views

urlpatterns = [
    url(r'^add-billing', views.add_billing, name='add-billing'),
    url(r'^add-postal-address', views.add_postal, name='add-postal'),
]
