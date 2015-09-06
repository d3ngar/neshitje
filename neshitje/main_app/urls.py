from django.conf.urls import url, patterns, include

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^register', views.register, name='register'),
    url(r'^my-account', views.account, name='account'),
]
