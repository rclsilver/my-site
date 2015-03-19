# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from my_resume.views import DownloadView, FormationsView, SkillsView, JobsView, HobbiesView, DownloadPdfView


urlpatterns = patterns("",
    url(r"^telechargement\.html$", DownloadView.as_view(), name="download"),
    url(r"^curriculum-vitae\.pdf$", DownloadPdfView.as_view(), name="download-pdf"),
    url(r"^diplomes\.html$", FormationsView.as_view(), name="formations"),
    url(r"^competences\.html$", SkillsView.as_view(), name="skills"),
    url(r"^experiences\.html$", JobsView.as_view(), name="jobs"),
    url(r"^loisirs\.html$", HobbiesView.as_view(), name="hobbies"),
)
