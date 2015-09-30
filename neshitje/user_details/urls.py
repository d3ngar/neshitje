from django.conf.urls import url, patterns, include

from . import views

urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^add-billing-address', views.add_billing, name='add-billing'),
    url(r'^add-postal-address', views.add_postal, name='add-postal'),
    url(r'^postal-done', views.postal_done, name='postal-done'),
    url(r'^my-account', views.account, name='account'),
    url(r'^simple-form', views.simple_form, name='simple-form'),
    url(r'^login', views.login_process, name='login'),
    url(r'^logout', views.logout_process, name='logout'),
]
