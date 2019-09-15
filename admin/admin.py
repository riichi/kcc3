import itertools

from django.contrib import admin


class Kcc3AdminSite(admin.AdminSite):
    index_title = 'Home'

    def get_app_list(self, request):
        apps = super().get_app_list(request)

        grouped_apps = ('badges', 'chombos', 'common')
        group_filter = lambda x: x['app_label'] in grouped_apps
        first_party = filter(group_filter, apps)
        third_party = itertools.filterfalse(group_filter, apps)

        models = list(itertools.chain(*map(lambda x: x['models'], first_party)))

        kcc3_app = {
            'name': 'Mahjong',
            'app_label': 'kcc3',
            'app_url': '',
            'has_module_perms': True,
            'models': models,
        }

        return itertools.chain([kcc3_app], third_party)
