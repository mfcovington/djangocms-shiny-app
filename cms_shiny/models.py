from django.db import models
from filer.fields.image import FilerImageField

class ShinyApp(models.Model):

    class Meta:
        ordering = ['name']
        verbose_name = 'Shiny App'
        verbose_name_plural = 'Shiny Apps'

    name = models.CharField(
        help_text='Enter a brief, yet descriptive name for the Shiny app.',
        max_length=64,
    )

    description = models.TextField(
        help_text='Describe the Shiny app in more detail.',
    )

    url = models.URLField(
        help_text="Shiny apps are included as iframe elements. Specify the app's URL.",
    )

    repo = models.URLField(
        blank=True,
        help_text="Specify the URL of the Shiny app's repository (e.g., GitHub, Bitbucket, etc.).",
    )

    image = FilerImageField(
        blank=True,
        help_text='Upload a screenshot of the Shiny app.',
    )

    publish = models.BooleanField(
        default=True,
        help_text='Show Shiny app on site?'
    )

    slug = models.SlugField(u'slug',
        default='',
        help_text='Please enter a unique slug for this Shiny app. This should get auto-generated.',
        max_length=64,
    )

    def __str__(self):
        return self.name
