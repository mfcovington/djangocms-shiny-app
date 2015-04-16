# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from cms_shiny.menu import ShinyAppsMenu

class ShinyAppsApp(CMSApp):
    name = _("Shiny Apps App")
    urls = ["cms_shiny.urls"]
    app_name = "cms_shiny"
    menus = [ShinyAppsMenu]

apphook_pool.register(ShinyAppsApp)
