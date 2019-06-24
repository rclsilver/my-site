# -*- coding: utf-8 -*-
from django import template
from django.urls import reverse_lazy


register = template.Library()


@register.simple_tag
def resume_formations_url():
    return reverse_lazy("resume:formations")


@register.simple_tag
def resume_skills_url():
    return reverse_lazy("resume:skills")


@register.simple_tag
def resume_jobs_url():
    return reverse_lazy("resume:jobs")


@register.simple_tag
def resume_hobbies_url():
    return reverse_lazy("resume:hobbies")


@register.simple_tag
def resume_download_url():
    return reverse_lazy("resume:download")


@register.simple_tag
def resume_download_pdf_url():
    return reverse_lazy("resume:download-pdf")


@register.filter
def skill_level(skill):
    min_l = 0
    max_l = 4
    return int(skill.level / ((max_l - min_l) * 1.0) * 100)


@register.filter
def skills_by_category(skills):
    skills_array = {}
    for skill in skills.all():
        skills_array.setdefault(skill.category, []).append(skill)
    return tuple((c, tuple(s)) for c, s in skills_array.items())


@register.filter
def skills_list(skills):
    return ", ".join(tuple(s.label for s in skills))


@register.filter
def hobbies_list(hobbies):
    return ", ".join(tuple(h.name for h in hobbies))
