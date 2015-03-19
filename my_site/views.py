# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "my_site/home.html"


class ContactView(TemplateView):
    template_name = "my_site/contact.html"
    
    def get_context_data(self, **kwargs):
        from django.conf import settings
        return super(ContactView, self).get_context_data(
            email=settings.CONTACT_EMAIL,
            phone=settings.CONTACT_PHONE,
            linked_in=settings.CONTACT_LINKED_IN,
            **kwargs
        )


class VcardView(TemplateView):
    template_name = "my_site/vcard.vcf"
    
    def get_context_data(self, **kwargs):
        from django.conf import settings
        return super(VcardView, self).get_context_data(
            first_name=settings.CONTACT_FNAME,
            last_name=settings.CONTACT_LNAME,
            email=settings.CONTACT_EMAIL,
            phone=settings.CONTACT_PHONE,
            **kwargs
        )

    def get(self, request, *args, **kwargs):
        response = super(VcardView, self).get(request, *args, **kwargs)
        response["Content-Type"] = "text/x-vcard"
        response["Content-Disposition"]= "inline; filename=\"%s\"" % (request.path.split("/")[-1:][0],)
        return response


class RobotsView(TemplateView):
    template_name = "my_site/robots.txt"

    def get(self, request, *args, **kwargs):
        response = super(RobotsView, self).get(request, *args, **kwargs)
        response["Content-Type"] = "text/plain"
        return response
