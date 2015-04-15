# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_shiny', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shinyapp',
            options={'ordering': ['name'], 'verbose_name_plural': 'Shiny Apps', 'verbose_name': 'Shiny App'},
        ),
    ]
