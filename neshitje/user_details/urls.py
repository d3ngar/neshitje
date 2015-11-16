from django.conf.urls import url, patterns, include

from . import views

urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^add-billing-address', views.add_billing, name='add-billing'),
    url(r'^add-postal-address', views.add_postal, name='add-postal'),
    url(r'^my-account', views.account, name='account'),
    url(r'^login', views.login_process, name='login'),
    url(r'^logout', views.logout_process, name='logout'),
    url(r'^logging', views.logging, name='logging'),
    url(r'^delete-postal', views.delete_postal, name='del-postal'),
    url(r'^edit-email', views.edit_email, name='edit-email'),
    url(r'^edit-password', views.edit_password, name='edit-password'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^edit-marketing', views.switch_marketing, name='edit-marketing'),
    url(r'^edit-name', views.edit_name, name='edit-name'),
    url(r'^edit-account-status', views.switch_account_status, name='status-switch'),
    url(r'^edit-phone', views.edit_phone, name='edit-phone'),
    # for password reset
    url(r'^reset-password$','django.contrib.auth.views.password_reset', {'post_reset_redirect' : 'user_details:password_reset_done', 'template_name': 'user_details/reset_password.html', 'email_template_name':'user_details/pwd_reset_email.html'}, name="password_reset"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+$)', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : 'user_details:password_reset_complete', 'template_name' : 'user_details/pwd_reset_new.html'}, name='password_reset_confirm'),
    url(r'^reset-done', 'django.contrib.auth.views.password_reset_done', {'template_name' : 'user_details/pwd_reset_done.html'}, name='password_reset_done'),
    url(r'^pwd-reset-complete', 'django.contrib.auth.views.password_reset_done', {'template_name' : 'user_details/pwd_reset_new_done.html'}, name='password_reset_complete'),
]
