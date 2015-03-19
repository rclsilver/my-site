# -*- coding: utf-8 -*-
from django.contrib import admin
from my_resume.forms import SkillCategoryForm, SkillForm, FormationForm, HobbyCategoryForm, HobbyForm, LanguageForm, EmployerForm, CustomerForm, JobForm
from my_resume.models import SkillCategory, Skill, Formation, HobbyCategory, Hobby, Language, Employer, Customer, Job


class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("label", "order", "skills_labels",)
    form = SkillCategoryForm
    
admin.site.register(SkillCategory, SkillCategoryAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ("label", "category", "level",)
    form = SkillForm
    
admin.site.register(Skill, SkillAdmin)


class FormationAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date",)
    form = FormationForm
    
admin.site.register(Formation, FormationAdmin)


class HobbyCategoryAdmin(admin.ModelAdmin):
    list_display = ("label", "order", "hobbies_labels",)
    form = HobbyCategoryForm
    
admin.site.register(HobbyCategory, HobbyCategoryAdmin)


class HobbyAdmin(admin.ModelAdmin):
    list_display = ("name", "category",)
    form = HobbyForm
    
admin.site.register(Hobby, HobbyAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "reading", "writing", "speaking",)
    form = LanguageForm
    
admin.site.register(Language, LanguageAdmin)


class EmployerAdmin(admin.ModelAdmin):
    list_display = ("name", "jobs_count",)
    form = EmployerForm
    
admin.site.register(Employer, EmployerAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "jobs_count",)
    form = CustomerForm
    
admin.site.register(Customer, CustomerAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "start_date", "end_date", "employer", "customer",)
    form = JobForm
    
admin.site.register(Job, JobAdmin)
