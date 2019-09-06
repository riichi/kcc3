from django.contrib import admin

from common.models import Player


class PlayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerAdmin)
