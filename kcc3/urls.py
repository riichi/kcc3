"""kcc3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import badges.urls
import chombos.urls
import common.urls
from badges.viewsets import BadgeViewSet
from chombos.viewsets import ChomboViewSet
from common.viewsets import PlayerViewSet

router = routers.DefaultRouter()
router.register('chombos', ChomboViewSet)
router.register('badges', BadgeViewSet)
router.register('players', PlayerViewSet)

admin_urlpatterns = [
    path('badges/', include(badges.urls.admin_urlpatters)),
    path('', admin.site.urls),
]

badgeclients_urlpatterns = [
    path('badges/', include(badges.urls.badgeclients_urlpatterns)),
    path('chombos/', include(chombos.urls.badgeclients_urlpatterns)),
]

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', include(admin_urlpatterns)),
    path('badge-clients/', include(badgeclients_urlpatterns)),

    path('badges/', include(badges.urls.urlpatterns)),
    path('', include(common.urls.urlpatterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
