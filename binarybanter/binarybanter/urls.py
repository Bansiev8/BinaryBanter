from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, serve
from django.urls import include, re_path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('authcontrol.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, })
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)