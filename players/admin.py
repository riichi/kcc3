from django.contrib import admin

from players.models import Player


class PlayerAdmin(admin.ModelAdmin):
    search_fields = (
        'first_name', 'last_name', 'nickname', 'usma_id', 'discord_id')
    list_display = (
        'user', 'first_name', 'last_name', 'nickname', 'usma_id', 'discord_id')
    list_display_links = ('first_name', 'last_name', 'nickname')


admin.site.register(Player, PlayerAdmin)
