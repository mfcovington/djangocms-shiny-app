# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_migrate_use_structure'),
        ('cms_shiny', '0004_auto_20150415_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShinyAppPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', parent_link=True)),
                ('shiny_app', models.ForeignKey(to='cms_shiny.ShinyApp', related_name='plugins')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
