from django.conf.urls import patterns, include, url
from django.contrib import admin

from filebrowser.sites import site

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'demo17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ublocks/', include('django-ublocks.urls')),
)
