# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cms_shiny.models import ShinyAppPluginModel

class ShinyAppPlugin(CMSPluginBase):
    model = ShinyAppPluginModel
    module = "Lab Plugins"
    name = _("Shiny App Plugin")
    render_template = "cms_shiny/plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(ShinyAppPlugin)
