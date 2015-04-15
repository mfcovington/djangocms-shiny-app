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


class ShinyAppDetailView(DetailView):
    model = ShinyApp
    template_name = 'cms_shiny/shiny_detail.html'
    context_object_name = 'shiny_app'
