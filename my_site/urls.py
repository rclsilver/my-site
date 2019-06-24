# -*- coding: utf-8 -*-
from django.urls import path, include
from django.contrib import admin

from my_site.views import HomeView, ContactView, VcardView, RobotsView


admin.autodiscover()

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thomas-betrancourt.vcf', VcardView.as_view(), name='vcard'),
    path('contact.html', ContactView.as_view(), name='contact'),
    path('robots.txt', RobotsView.as_view(), name='robots'),
    path('cv/', include('my_resume.urls', namespace='resume')),
    path('admin/', admin.site.urls),
    path('health/', include('health_check.urls')),
]