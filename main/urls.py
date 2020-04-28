from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.urls import include, path
from djavError.urls import djaverror_urls

from example.urls import example_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(auth_urls)),
    path('', include(example_urls)),
    path('', include(djaverror_urls))
]
