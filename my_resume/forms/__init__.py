# -*- coding: utf-8 -*-
from django import forms
from my_resume.forms.widgets import SkillsSelectWidget
from my_resume.models import SkillCategory, Skill, Customer, Employer, Job, Formation, HobbyCategory, Hobby, Language


class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = "__all__"


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = "__all__"


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        widgets = {
            "skills": SkillsSelectWidget
        }


class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = "__all__"


class HobbyCategoryForm(forms.ModelForm):
    class Meta:
        model = HobbyCategory
        fields = "__all__"


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = "__all__"


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = "__all__"
