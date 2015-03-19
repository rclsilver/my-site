# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin

from my_site.views import HomeView, ContactView, VcardView, RobotsView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^thomasbetrancourt\.vcf$', VcardView.as_view(), name='vcard'),
    url(r'^contact\.html$', ContactView.as_view(), name='contact'),
    url(r'^robots\.txt$', RobotsView.as_view(), name='robots'),
    url(r'^cv/', include('my_resume.urls', namespace='resume')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)