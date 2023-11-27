from collections.abc import Iterable
from typing import ClassVar

from django.contrib import admin

from club.models import Member, MemberRole, MembershipFeePeriod


class MemberRoleInline(admin.TabularInline):
    model = MemberRole


class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields: ClassVar[dict[str, Iterable[str]]] = {"id": ("first_name", "last_name")}

    search_fields = ("id", "first_name", "last_name", "nickname")
    list_display = ("id", "first_name", "last_name", "nickname", "active_since", "active_until")
    list_display_links = ("id", "first_name", "last_name", "nickname")
    ordering = ("last_name", "first_name")

    inlines = (MemberRoleInline,)


class MembershipFeePeriodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Member, MemberAdmin)
admin.site.register(MembershipFeePeriod, MembershipFeePeriodAdmin)
