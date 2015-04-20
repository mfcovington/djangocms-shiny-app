from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from cms_shiny.models import ShinyApp

class ShinyAppListView(ListView):
    model = ShinyApp
    template_name = 'cms_shiny/shiny_list.html'
    context_object_name = 'published_shiny_apps'

    def get_queryset(self):
        """Return all published Shiny apps."""
        return ShinyApp.objects.filter(publish=True)


    def render_to_response(self, context, **response_kwargs):
        # Shim to affect the CMS Toolbar only
        if self.request.toolbar:

            menu = self.request.toolbar.get_or_create_menu('shiny-apps-list-menu', 'Shiny Apps')

            url_change = reverse('admin:cms_shiny_shinyapp_changelist')
            url_addnew = reverse('admin:cms_shiny_shinyapp_add')
            menu.add_sideframe_item('Edit Shiny Apps', url=url_change)
            menu.add_modal_item('Add New Shiny App', url=url_addnew)

        return super(ShinyAppListView, self).render_to_response(context, **response_kwargs)


class ShinyAppDetailView(DetailView):
    model = ShinyApp
    template_name = 'cms_shiny/shiny_detail.html'
    context_object_name = 'shiny_app'

    def render_to_response(self, context, **response_kwargs):
        # Shim to affect the CMS Toolbar only
        if self.request.toolbar:

            menu = self.request.toolbar.get_or_create_menu('shiny-apps-detail-menu', self.object.name)

            url_change = reverse('admin:cms_shiny_shinyapp_change', args=[self.object.id])
            url_delete = reverse('admin:cms_shiny_shinyapp_delete', args=[self.object.id])
            menu.add_modal_item('Edit %s' % self.object.name, url=url_change)
            menu.add_modal_item('Delete %s' % self.object.name, url=url_delete)

        return super(ShinyAppDetailView, self).render_to_response(context, **response_kwargs)
