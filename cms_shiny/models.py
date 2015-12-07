from django.db import models
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin

def clickable(url):
    """This returns a clickable HTML anchor that opens in a new tab"""
    return "<a href={0} target='_blank'>{0}</a>".format(url)

class ShinyApp(models.Model):

    class Meta:
        ordering = ['name']
        verbose_name = 'Shiny App'
        verbose_name_plural = 'Shiny Apps'

    name = models.CharField(
        help_text='Enter a brief, yet descriptive name for the Shiny app.',
        max_length=64,
        unique=True,
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
        null=True,
        blank=True,
        help_text='Upload a screenshot of the Shiny app.',
    )

    publish = models.BooleanField(
        default=True,
        help_text='Show Shiny app on site?'
    )

    slug = models.SlugField(u'slug',
        help_text='Please enter a unique slug for this Shiny app. This should get auto-generated.',
        max_length=64,
        unique=True,
    )

    def clickable_url(self):
        return clickable(self.url)

    clickable_url.allow_tags = True
    clickable_url.short_description = "Shiny App URL"

    def clickable_repo(self):
        return clickable(self.repo)

    clickable_repo.allow_tags = True
    clickable_repo.short_description = "Shiny App Code Repository"

    def __str__(self):
        return self.name


class ShinyAppPluginModel (CMSPlugin):
    shiny_app = models.ForeignKey('cms_shiny.ShinyApp',
        related_name='plugins'
    )

    def __str__(self):
        return self.shiny_app.name
