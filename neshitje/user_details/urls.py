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
    url(r'^logging', views.logging, name='logging'),
    url(r'^delete-postal', views.delete_postal, name='del-postal'),
    url(r'^edit-email', views.edit_email, name='edit-email'),
    url(r'^edit-password', views.edit_password, name='edit-password'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^reset-password', views.reset_password, name='reset-password'),
    url(r'^edit-marketing', views.switch_marketing, name='edit-marketing'),
    url(r'^edit-name', views.edit_name, name='edit-name'),
    url(r'^edit-account-status', views.switch_account_status, name='status-switch'),
]
