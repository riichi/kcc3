from django.contrib import admin

from common.models import Player


class PlayerProfile(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerProfile)
