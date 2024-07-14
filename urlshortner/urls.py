
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^static/(.*)$', serve, {'document.root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
