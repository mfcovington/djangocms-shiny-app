# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms_shiny', '0003_shinyapp_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shinyapp',
            name='image',
            field=filer.fields.image.FilerImageField(null=True, to='filer.Image', help_text='Upload a screenshot of the Shiny app.', blank=True),
            preserve_default=True,
        ),
    ]
