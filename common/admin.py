from django.contrib import admin

from common.models import Player


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')


admin.site.register(Player, PlayerAdmin)
