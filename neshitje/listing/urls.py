from django.conf.urls import url, patterns, include
from . import views

urlpatterns = [
    url(r'^listing-sample', views.listing, name='listing'),
    url(r'^edit-listing', views.edit_listing, name='edit-listing'),
    url(r'^upload-images', views.image_upload, name='image-upload'),
    url(r'^item/(?P<listing_id>\S+)/$', views.view_listing, name='view-listing'),
    url(r'^view-all-categories', views.category_tree, name='category_tree'),
]
