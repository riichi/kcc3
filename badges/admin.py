from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.html import format_html

from badges.models import Badge


class IsAutomaticFilter(SimpleListFilter):
    title = 'automatic'
    parameter_name = 'automatic'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Yes'),
            ('0', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.automatic()
        elif self.value() == '0':
            return queryset.not_automatic()

        return queryset


class BadgeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'id': ('title',)}
    autocomplete_fields = ('owners', 'players')
    readonly_fields = ('token',)

    list_display = ('image_tag', 'id', 'title', 'automatic', 'description')
    list_display_links = ('image_tag', 'id', 'title')
    list_filter = ('owners', IsAutomaticFilter)
    search_fields = ('id', 'title', 'description')
    ordering = ('id',)

    view_on_site = True

    def image_tag(self, obj):
        return format_html(
            f'<img src="{obj.image.url}"'
            f' style="max-width: 48px; max-height: 48px;" />')

    image_tag.short_description = 'Image'

    def automatic(self, obj):
        return obj.is_automatic

    automatic.boolean = True

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs
        return qs.filter(owners=request.user)

    def get_fieldsets(self, request, obj=None):
        general_fields = ['title', 'id', 'description', 'image']
        if request.user.is_superuser or obj is not None:
            general_fields.append('owners')
        general_fields += ['players']

        return (
            (None, {
                'fields': general_fields
            }),
            ('Endpoint', {
                'fields': ('endpoint_url', 'refresh_interval', 'token'),
            }),
        )

    def get_changeform_initial_data(self, request):
        return {'owners': (request.user,)}

    def get_readonly_fields(self, request, obj=None):
        fields = super(BadgeAdmin, self).get_readonly_fields(request, obj)

        if not request.user.is_superuser:
            fields = fields + ('owners',)

        return fields

    def save_related(self, request, form, formsets, change):
        super(BadgeAdmin, self).save_related(request, form, formsets, change)

        if not form.instance.owners.exists():
            form.instance.owners.add(request.user)


admin.site.register(Badge, BadgeAdmin)
