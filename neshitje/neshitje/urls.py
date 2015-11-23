from django.conf.urls import patterns, include, url
from django.contrib import admin
#from main_app.views import homepage

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', homepage, name='homepage'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('main_app.urls', namespace="main_app")),
    url(r'^listing/', include('listing.urls', namespace="listing")),
    url(r'^search/', include('search.urls', namespace="search")),
    url(r'^user_details/', include('user_details.urls', namespace="user_details")),
    #url(r'^order/', include('order.urls', namespace="order")),
    url(r'^', include('main_app.urls', namespace = "main_app")),
    # for testing
)
