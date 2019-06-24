# -*- coding: utf-8 -*-
from django.urls import path
from my_resume.views import DownloadView, FormationsView, SkillsView, JobsView, HobbiesView, DownloadPdfView

app_name = 'resume'

urlpatterns = [
    path('telechargement.html', DownloadView.as_view(), name='download'),
    path('curriculum-vitae.pdf', DownloadPdfView.as_view(), name='download-pdf'),
    path('diplomes.html', FormationsView.as_view(), name='formations'),
    path('competences.html', SkillsView.as_view(), name='skills'),
    path('experiences.html', JobsView.as_view(), name='jobs'),
    path('loisirs.html', HobbiesView.as_view(), name='hobbies'),
]