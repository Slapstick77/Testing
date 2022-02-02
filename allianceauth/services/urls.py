from django.conf.urls import include
from allianceauth.hooks import get_hooks
from django.urls import re_path

from . import views

urlpatterns = [
    # Services
    re_path(r'^services/', include(([
        re_path(r'^$', views.services_view, name='services'),
        # Tools
        re_path(r'^tool/fleet_formatter_tool/$', views.fleet_formatter_view, name='fleet_format_tool'),
    ], 'services'), namespace='services')),
]

# Append hooked service urls
services = get_hooks('services_hook')
for svc in services:
    urlpatterns += svc().urlpatterns
