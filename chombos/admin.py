from django.contrib import admin

from chombos.models import Chombo


class ChomboAdmin(admin.ModelAdmin):
    search_fields = (
        "player__id",
        "player__first_name",
        "player__last_name",
        "player__nickname",
        "timestamp",
        "comment",
    )
    list_display = ("player", "timestamp", "comment")
    list_display_links = ("player", "timestamp")
    list_filter = (
        "timestamp",
        ("player", admin.RelatedOnlyFieldListFilter),
    )
    ordering = ("-timestamp",)
    date_hierarchy = "timestamp"


admin.site.register(Chombo, ChomboAdmin)
