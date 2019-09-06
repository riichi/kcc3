from django.contrib import admin

from chombos.models import Chombo


class ChomboAdmin(admin.ModelAdmin):
    pass


admin.site.register(Chombo, ChomboAdmin)
