# -*- coding: utf-8 -*-
from django.http.response import HttpResponse
from django.template.context import RequestContext
from django.template.loader import get_template
from django.views.generic.base import TemplateView, View, ContextMixin
from io import BytesIO
from xhtml2pdf import pisa

from my_resume.models import Formation, Skill, Job, HobbyCategory, Language


class FormationsView(TemplateView):
    template_name = "my_resume/formations.html"
    
    def get_context_data(self, **kwargs):
        return super(TemplateView, self).get_context_data(formations=Formation.objects.all(), **kwargs)


class SkillsView(TemplateView):
    template_name = "my_resume/skills.html"
    
    def get_context_data(self, **kwargs):
        return super(TemplateView, self).get_context_data(skills=Skill.objects.filter(level__isnull=False), **kwargs)


class JobsView(TemplateView):
    template_name = "my_resume/jobs.html"
    
    def get_context_data(self, **kwargs):
        return super(TemplateView, self).get_context_data(jobs=Job.objects.all(), **kwargs)


class HobbiesView(TemplateView):
    template_name = "my_resume/hobbies.html"
    
    def get_context_data(self, **kwargs):
        return super(TemplateView, self).get_context_data(hobbies=HobbyCategory.objects.all(), **kwargs)


class DownloadView(TemplateView):
    template_name = "my_resume/download.html"


class DownloadPdfView(ContextMixin, View):
    template_name = "my_resume/export.html"
    
    def link_callback(self, uri, rel):
        import os
        from django.conf import settings
        
        # use short variable names
        sUrl = settings.STATIC_URL
        sRoot = settings.STATIC_ROOT
    
        # convert URIs to absolute system paths
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
        
        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception("media URI must start with %s" % (sUrl))
        
        return path

    def get_context_data(self, **kwargs):
        return super(DownloadPdfView, self).get_context_data(
            formations=Formation.objects.all(),
            skills=Skill.objects.filter(level__isnull=False),
            jobs=Job.objects.all(),
            hobbies=HobbyCategory.objects.all(),
            languages=Language.objects.all(),
            **kwargs
        )

    def get(self, request, *args, **kwargs):
        # Génération du contenu HTML
        template = get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        html = template.render(
            RequestContext(request, context).flatten()
        )

        # Génération du contenu PDF
        pdf_file = BytesIO()
        pisa.CreatePDF(
            html,
            dest=pdf_file,
            link_callback=self.link_callback
        )
        pdf = pdf_file.getvalue()
        pdf_file.close()
        
        # Construction de la réponse
        force_dl = str(request.GET.get("force-dl", 1))
        
        if force_dl in [1, 'true', '1', 'y']:
            response = HttpResponse(pdf, content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="CV - Thomas BETRANCOURT.pdf"'
        else:
            response = HttpResponse(pdf, content_type='application/pdf')
        
        return response
