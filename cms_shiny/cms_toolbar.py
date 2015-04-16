# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break, SubMenu
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK

@toolbar_pool.register
class ShinyAppsToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(
            ADMIN_MENU_IDENTIFIER, _('Apps')
        )

        position = admin_menu.get_alphabetical_insert_position(
            _('Shiny Apps'),
            SubMenu
        )

        if not position:
            position = admin_menu.find_first(
                Break,
                identifier=ADMINISTRATION_BREAK
            ) + 1
            admin_menu.add_break('custom-break', position=position)

        shiny_apps_menu = admin_menu.get_or_create_menu(
            'shiny-apps-menu',
            _('Shiny Apps ...'),
            position=position
        )

        url_change = reverse('admin:cms_shiny_shinyapp_changelist')
        url_addnew = reverse('admin:cms_shiny_shinyapp_add')
        shiny_apps_menu.add_sideframe_item(_('Edit Shiny Apps'), url=url_change)
        shiny_apps_menu.add_modal_item(_('Add New Shiny App'), url=url_addnew)
