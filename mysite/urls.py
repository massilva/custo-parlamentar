from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alba.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
