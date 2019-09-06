from django.contrib import admin

from badges.models import Badge


class BadgeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"id": ("title",)}


admin.site.register(Badge, BadgeAdmin)
