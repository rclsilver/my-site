# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'employer',
            },
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name='title')),
                ('location', models.CharField(max_length=64, verbose_name='location')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(null=True, verbose_name='end date', blank=True)),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'ordering': ('-start_date',),
                'verbose_name': 'formation',
            },
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'hobby',
                'verbose_name_plural': 'hobbies',
            },
        ),
        migrations.CreateModel(
            name='HobbyCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(unique=True, max_length=32, verbose_name='label')),
                ('icon_class', models.CharField(max_length=32, null=True, verbose_name='icon class', blank=True)),
                ('order', models.IntegerField(default=0, verbose_name='order')),
            ],
            options={
                'ordering': ('order', 'label'),
                'verbose_name': 'hobbies category',
                'verbose_name_plural': 'hobbies categories',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('location', models.CharField(max_length=32, verbose_name='location')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(null=True, verbose_name='end date', blank=True)),
                ('short_description', models.TextField(verbose_name='short description')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('nl_after', models.BooleanField(default=False, verbose_name='new line after')),
                ('customer', models.ForeignKey(related_name='jobs', verbose_name='customer', blank=True, to='my_resume.Customer', null=True)),
                ('employer', models.ForeignKey(related_name='jobs', verbose_name='employer', to='my_resume.Employer')),
            ],
            options={
                'ordering': ('-start_date',),
                'verbose_name': 'job',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='name')),
                ('reading', models.BooleanField(verbose_name='reading')),
                ('writing', models.BooleanField(verbose_name='writing')),
                ('speaking', models.BooleanField(verbose_name='speaking')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'language',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(unique=True, max_length=32, verbose_name='label')),
                ('level', models.PositiveIntegerField(blank=True, null=True, verbose_name='level', choices=[(1, 'beginner'), (2, 'intermediate'), (3, 'experienced'), (4, 'expert')])),
            ],
            options={
                'ordering': ('category', 'label'),
                'verbose_name': 'skill',
            },
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(unique=True, max_length=32, verbose_name='label')),
                ('order', models.IntegerField(default=0, verbose_name='order')),
            ],
            options={
                'ordering': ('order', 'label'),
                'verbose_name': 'skills category',
                'verbose_name_plural': 'skills categories',
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(related_name='skills', verbose_name='category', to='my_resume.SkillCategory'),
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(related_name='jobs', verbose_name='skills', to='my_resume.Skill', blank=True),
        ),
        migrations.AddField(
            model_name='hobby',
            name='category',
            field=models.ForeignKey(related_name='hobbies', verbose_name='category', to='my_resume.HobbyCategory'),
        ),
    ]
