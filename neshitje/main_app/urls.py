from django.conf.urls import url, patterns, include

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^contact-us$', views.contact, name='contact'),
]
