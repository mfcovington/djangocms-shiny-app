# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from cms_shiny.models import ShinyApp

class ShinyAppsMenu(CMSAttachMenu):
    name = _("Shiny Apps Menu")

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for shiny_app in ShinyApp.objects.all():
            node = NavigationNode(
                shiny_app.name,
                reverse('cms_shiny:shiny_detail', args=(shiny_app.slug,)),
                shiny_app.slug
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(ShinyAppsMenu)
