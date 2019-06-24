# -*- coding: utf-8 -*-
from django import template
from django.urls import reverse_lazy, resolve
import re


register = template.Library()


def current_url_equals(context, url_name, **kwargs):
    resolved = False
    try:
        resolved = resolve(context.get("request").path)
    except:
        pass
    
    current_url = False
    
    if resolved and resolved.namespace:
        current_url = "%s:%s" % (resolved.namespace, resolved.url_name)
    elif resolved:
        current_url = resolved.url_name

    matches = current_url and re.match(url_name, current_url)

    if matches and kwargs:
        for key in kwargs:
            kwarg = kwargs.get(key)
            resolved_kwarg = resolved.kwargs.get(key)
            if not resolved_kwarg or kwarg != resolved_kwarg:
                return False

    return matches


@register.simple_tag(takes_context=True)
def current_page_class(context, url_name, return_value='active'):
    matches = current_url_equals(context, url_name)
    return return_value if matches else ""


@register.simple_tag
def home_url():
    return reverse_lazy("home")


@register.simple_tag
def contact_url():
    return reverse_lazy("contact")


@register.simple_tag
def vcard_url():
    return reverse_lazy("vcard")
