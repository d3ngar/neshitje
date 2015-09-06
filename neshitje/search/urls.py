from django.conf.urls import url, patterns, include

from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^results', views.search_results, name='search_results'),
]
