from django.contrib import admin

from chombos.models import Chombo


class ChomboAdmin(admin.ModelAdmin):
    search_fields = ('player', 'timestamp', 'comment')
    list_display = ('player', 'timestamp', 'comment')
    list_display_links = ('player', 'timestamp')


admin.site.register(Chombo, ChomboAdmin)
