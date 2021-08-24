from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("", include("users.urls")),
                  path("", include("posts.urls")),
                  path("", include("authentication.urls", namespace="authentication")),
                  path("", include("members.urls")),
                  path("", include("vacancies.urls")),
                  path("", include("polls.urls", namespace="polls")),
                  path("", include('calls.urls')),
                  path("", include("django.contrib.auth.urls")),
                  path("summernote/", include("django_summernote.urls")),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
