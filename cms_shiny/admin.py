from django.contrib import admin
from cms_shiny.models import ShinyApp

class ShinyAppAdmin(admin.ModelAdmin):

    fieldset_basic = ('Basic', {
        'fields': [
            'name',
            'description',
            'url',
            'repo',
            'image',
            'publish',
        ]
    })

    fieldset_advanced = ('Advanced', {
        'fields': ['slug'],
        'classes': ['collapse'],
    })

    fieldsets = [
        fieldset_basic,
        fieldset_advanced,
    ]

    list_display = ['name', 'clickable_url', 'clickable_repo', 'publish']
    list_filter = ['publish']
    search_fields = ['name', 'description']

    prepopulated_fields = {"slug": ("name",)}

admin.site.register(ShinyApp, ShinyAppAdmin)
