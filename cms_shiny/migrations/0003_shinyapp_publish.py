# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_shiny', '0002_auto_20150415_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='shinyapp',
            name='publish',
            field=models.BooleanField(default=True, help_text='Show Shiny app on site?'),
            preserve_default=True,
        ),
    ]
