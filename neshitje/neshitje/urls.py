from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'neshitje.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('main_app.urls', namespace="main_app")),
    url(r'^product/', include('product.urls', namespace="product")),
    url(r'^search/', include('search.urls', namespace="search")),
    url(r'^user_details/', include('user_details.urls', namespace="user_details")),
    #url(r'^order/', include('order.urls', namespace="order")),
    url(r'^', include('main_app.urls', namespace = "main_app")),
)
