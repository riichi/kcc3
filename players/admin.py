from collections.abc import Iterable
from typing import ClassVar

from django.contrib import admin

from players.models import Player


class PlayerAdmin(admin.ModelAdmin):
    prepopulated_fields: ClassVar[dict[str, Iterable[str]]] = {"id": ("nickname",)}

    search_fields = ("id", "first_name", "last_name", "nickname", "usma_id", "discord_id")
    list_display = ("id", "user", "first_name", "last_name", "nickname", "usma_id", "discord_id")
    list_display_links = ("id", "first_name", "last_name", "nickname")
    ordering = ("id",)


admin.site.register(Player, PlayerAdmin)
