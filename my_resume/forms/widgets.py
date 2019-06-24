# -*- coding: utf-8 -*-
from django.forms.widgets import CheckboxSelectMultiple
from my_resume.models import SkillCategory
from django.utils.safestring import mark_safe


class SkillsSelectWidget(CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        id_field = attrs["id"]
        choices = tuple((c.label, tuple(((s.id, s.label) for s in c.skills.all()))) for c in SkillCategory.objects.all())
        output = []

        for c in choices:
            output.append('<h2>{}</h2>'.format(c[0]))
            output.append('<ul>')

            for s in c[1]:
                output.append('<li>')
                output.append('  <label for="{}_{}">'.format(id_field, s[0]))
                output.append('    <input type="checkbox" id="{}_{}" name="{}" value="{}"{}></input> {}'.format(
                    id_field,
                    s[0],
                    name,
                    s[0],
                    ' checked' if value is not None and s[0] in value else '',
                    s[1],
                ))
                output.append('  </label>')
                output.append('</li>')

            output.append('</ul>')

        return mark_safe('\n'.join(output))
