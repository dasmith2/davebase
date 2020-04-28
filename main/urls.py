from django.conf import settings
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.urls import include, path
from djavError.urls import djaverror_urls

from example.urls import example_urls
from main.views import this_site_js


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(auth_urls)),
    path('js/this_site.js', this_site_js, name='this_site_js'),
    path('', include(example_urls)),
    path('', include(djaverror_urls))
]

if settings.DEBUG:
  import debug_toolbar
  urlpatterns += [path('', include(debug_toolbar.urls))]
