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

    prepopulated_fields = {"slug": ("name",)}

admin.site.register(ShinyApp, ShinyAppAdmin)
