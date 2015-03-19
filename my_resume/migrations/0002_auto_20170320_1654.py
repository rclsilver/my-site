# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='formation',
            name='title',
            field=models.CharField(max_length=64, verbose_name='title'),
        ),
    ]
