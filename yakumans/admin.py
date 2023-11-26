from django import forms
from django.contrib import admin
from django.contrib.admin import FieldListFilter
from django.core.files import File

from yakumans import yakumans
from yakumans.metadata_stripper import strip_exif
from yakumans.models import Yakuman


class YakumanFilter(FieldListFilter):
    title = "yaku"

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg = field_path
        self.lookup_val = params.get(self.lookup_kwarg)
        super().__init__(field, request, params, model, model_admin, field_path)

    def lookups(self, request, model_admin):
        return ((yaku.id, yaku.name) for yaku in yakumans.YAKUMANS_BY_NAME)

    def queryset(self, request, queryset):
        if self.lookup_val:
            return queryset.filter(yaku__contains=f"{self.lookup_val};")

        return queryset

    def expected_parameters(self):
        return [self.lookup_kwarg]

    def choices(self, changelist):
        yield {
            "selected": self.lookup_val is None,
            "query_string": changelist.get_query_string(remove=[self.lookup_kwarg]),
            "display": "All",
        }
        for yaku in yakumans.YAKUMANS_BY_NAME:
            yield {
                "selected": self.lookup_val == yaku.id,
                "query_string": changelist.get_query_string({self.lookup_kwarg: yaku.id}),
                "display": yaku.name,
            }


class YakumanAdminForm(forms.ModelForm):
    def clean_picture(self):
        orig_file = self.cleaned_data["picture"]
        if orig_file is None:
            return orig_file

        orig_file_name = orig_file.name

        new_image = strip_exif(orig_file)
        new_file = File(new_image)
        new_file.name = orig_file_name

        return new_file


class YakumanAdmin(admin.ModelAdmin):
    form = YakumanAdminForm
    search_fields = (
        "winner__id",
        "winner__first_name",
        "winner__last_name",
        "winner__nickname",
        "loser__id",
        "loser__first_name",
        "loser__last_name",
        "loser__nickname",
        "timestamp",
        "yaku",
        "comment",
    )
    list_display = ("timestamp", "yaku", "winner", "loser")
    list_display_links = ("timestamp", "winner")
    list_filter = (
        "timestamp",
        ("yaku", YakumanFilter),
        ("winner", admin.RelatedOnlyFieldListFilter),
        ("loser", admin.RelatedOnlyFieldListFilter),
    )
    ordering = ("-timestamp",)
    date_hierarchy = "timestamp"


admin.site.register(Yakuman, YakumanAdmin)
