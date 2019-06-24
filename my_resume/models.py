# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class SkillCategory(models.Model):
    label = models.CharField(_("label"), max_length=32, unique=True)
    order = models.IntegerField(_("order"), default=0)
    
    def skills_labels(self):
        return ", ".join(list((s.label for s in self.skills.all())))
    
    def __str__(self):
        return self.label
    
    class Meta:
        ordering = ("order", "label",)
        verbose_name = _("skills category")
        verbose_name_plural = _("skills categories")


class Skill(models.Model):
    LEVEL_1 = _("beginner")
    LEVEL_2 = _("intermediate")
    LEVEL_3 = _("experienced")
    LEVEL_4 = _("expert")
    LEVEL_CHOICES = (
        (1, LEVEL_1),
        (2, LEVEL_2),
        (3, LEVEL_3),
        (4, LEVEL_4),
    )
    
    label = models.CharField(_("label"), max_length=32, unique=True)
    level = models.PositiveIntegerField(_("level"), null=True, blank=True, choices=LEVEL_CHOICES)
    category = models.ForeignKey(SkillCategory, verbose_name=_("category"), related_name="skills", on_delete=models.CASCADE)
    
    @property
    def level_label(self):
        for l in Skill.LEVEL_CHOICES:
            if self.level == l[0]:
                return l[1]

    def __str__(self):
        return self.label

    class Meta:
        ordering = ("category", "label",)
        verbose_name = _("skill")
        

class Customer(models.Model):
    name = models.CharField(_("name"), max_length=32, unique=True)
    
    def jobs_count(self):
        return self.jobs.count()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("name",)
        verbose_name = _("customer",)
    

class Employer(models.Model):
    name = models.CharField(_("name"), max_length=32, unique=True)
    
    def jobs_count(self):
        return self.jobs.count()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("name",)
        verbose_name = _("employer",)
    

class Job(models.Model):
    title = models.CharField(_("title"), max_length=64)
    location = models.CharField(_("location"), max_length=32)
    start_date = models.DateField(_("start date"))
    end_date = models.DateField(_("end date"), null=True, blank=True)
    employer = models.ForeignKey(Employer, verbose_name=_("employer"), related_name="jobs", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name=_("customer"), related_name="jobs", null=True, blank=True, on_delete=models.SET_NULL)
    short_description = models.TextField(_("short description"))
    description = models.TextField(_("description"), null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True, verbose_name=_("skills"), related_name="jobs")
    nl_after = models.BooleanField(_("new line after"), default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("-start_date",)
        verbose_name = _("job")
    

class Formation(models.Model):
    title = models.CharField(_("title"), max_length=64)
    location = models.CharField(_("location"), max_length=64)
    start_date = models.DateField(_("start date"))
    end_date = models.DateField(_("end date"), null=True, blank=True)
    description = models.TextField(_("description"), null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("-start_date",)
        verbose_name = _("formation",)


class HobbyCategory(models.Model):
    label = models.CharField(_("label"), max_length=32, unique=True)
    icon_class = models.CharField(_("icon class"), max_length=32, null=True, blank=True)
    order = models.IntegerField(_("order"), default=0)
    
    def hobbies_labels(self):
        return ", ".join(list((h.name for h in self.hobbies.all())))
    
    def __str__(self):
        return self.label
    
    class Meta:
        ordering = ("order", "label",)
        verbose_name = _("hobbies category")
        verbose_name_plural = _("hobbies categories")


class Hobby(models.Model):
    name = models.CharField(_("name"), max_length=32, unique=True)
    category = models.ForeignKey(HobbyCategory, verbose_name=_("category"), related_name="hobbies", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("name",)
        verbose_name = _("hobby",)
        verbose_name_plural = _("hobbies")
    

class Language(models.Model):
    name = models.CharField(_("name"), max_length=32, unique=True)
    reading = models.BooleanField(_("reading"))
    writing = models.BooleanField(_("writing"))
    speaking = models.BooleanField(_("speaking"))
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("name",)
        verbose_name = _("language",)
