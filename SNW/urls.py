from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("intranet.urls", namespace="intranet")),
    path("", include("polls.urls", namespace="polls")),
    path("", include("django.contrib.auth.urls")),
    path("summernote/", include("django_summernote.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
