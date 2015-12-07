# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_shiny', '0005_shinyapppluginmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shinyapp',
            name='name',
            field=models.CharField(max_length=64, unique=True, help_text='Enter a brief, yet descriptive name for the Shiny app.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shinyapp',
            name='slug',
            field=models.SlugField(verbose_name='slug', max_length=64, unique=True, help_text='Please enter a unique slug for this Shiny app. This should get auto-generated.'),
            preserve_default=True,
        ),
    ]
