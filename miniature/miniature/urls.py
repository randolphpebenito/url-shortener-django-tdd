from django.conf.urls import include, url
from django.contrib import admin
from url_short import views
#from dashing.utils import router

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/', include('dashing.urls')),
    url(r'^shorten/(?P<pk>[0-9]+)/$', views.show_url_shorten, name='url_shorten'),
    url(r'^(?P<urlshort>[a-zA-Z0-9]{7})/$', views.redirect_url_shorten, name='url_shorten_redirect'),

    url(r'^admin/', include(admin.site.urls)),
]
