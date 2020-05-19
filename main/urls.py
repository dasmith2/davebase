""" These urls apply to all sites. Put site-specific stuff in
main/this_site_urls.py """
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.urls import include, path
from djavError.urls import djaverror_urls

from main.views import all_sites_js
from main.this_site_urls import this_site_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(auth_urls)),
    path('js/all_sites.js', all_sites_js, name='all_sites_js'),
    path('', include(djaverror_urls)),
    path('', include(this_site_urls))
]

if settings.DEBUG:
  import debug_toolbar
  urlpatterns += [path('', include(debug_toolbar.urls))]
