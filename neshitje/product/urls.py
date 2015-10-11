from django.conf.urls import url, patterns, include

from . import views

urlpatterns = [
    url(r'^product-sample', views.product, name='product'),
    url(r'^edit-product', views.edit_product, name='edit-product'),
    url(r'^upload-images', views.image_upload, name='image-upload'),
    url(r'^item/(?P<product_id>\S+)/$', views.product_view, name='view-product')
]
