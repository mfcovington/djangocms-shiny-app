# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150414_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShinyApp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64, help_text='Enter a brief, yet descriptive name for the Shiny app.')),
                ('description', models.TextField(help_text='Describe the Shiny app in more detail.')),
                ('url', models.URLField(help_text="Shiny apps are included as iframe elements. Specify the app's URL.")),
                ('repo', models.URLField(help_text="Specify the URL of the Shiny app's repository (e.g., GitHub, Bitbucket, etc.).", blank=True)),
                ('slug', models.SlugField(max_length=64, help_text='Please enter a unique slug for this Shiny app. This should get auto-generated.', verbose_name='slug', default='')),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', help_text='Upload a screenshot of the Shiny app.', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
