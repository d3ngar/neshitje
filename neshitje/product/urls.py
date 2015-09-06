from django.conf.urls import url, patterns, include

from . import views

urlpatterns = [
    url(r'^product_sample', views.product, name='product'),
]
