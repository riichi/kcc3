from django.contrib import admin

from badges.models import Badge, Player


class BadgeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"id": ("title",)}


class PlayerProfile(admin.ModelAdmin):
    pass


admin.site.register(Badge, BadgeAdmin)
admin.site.register(Player, PlayerProfile)
