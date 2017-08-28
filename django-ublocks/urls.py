# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'test/(?P<ublock>[a-z0-9-]+)/', 'django-ublocks.views.test', name='ublocks_test'),
)
