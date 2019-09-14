from django.contrib import admin
from django.utils.html import format_html

from badges.models import Badge


class BadgeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'id': ('title',)}
    autocomplete_fields = ('owners', 'players')
    readonly_fields = ('token',)

    list_display = ('image_tag', 'id', 'title', 'automatic', 'description')
    list_display_links = ('image_tag', 'id', 'title')
    list_filter = ('owners',)
    search_fields = ('id', 'title', 'description')

    view_on_site = True

    fieldsets = (
        (None, {
            'fields': (
                'title', 'id', 'description', 'image', 'owners', 'players'
            )
        }),
        ('Endpoint', {
            'classes': ('collapse',),
            'fields': ('endpoint_url', 'refresh_interval', 'token'),
        }),
    )

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width: 40px; max-height: 40px;" />'.format(obj.image.url))

    def automatic(self, obj):
        return obj.is_automatic
    automatic.boolean = True

    image_tag.short_description = 'Image'


admin.site.register(Badge, BadgeAdmin)
