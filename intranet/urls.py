from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("", include("users.urls")),
                  path("", include("posts.urls")),
                  # path("", include("accounts.urls")),
                  path("", include("members.urls")),
                  path("", include("vacancies.urls")),
                  path("", include("polls.urls")),
                  path("", include('conference.urls')),
                  path("", include("django.contrib.auth.urls")),
                  path("summernote/", include("django_summernote.urls")),
                  path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
                  path("reset_password/", auth_views.PasswordResetView.as_view(template_name="../templates/registration/password_reset.html"),name="reset_password",),
                  path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="../templates/registration/password_reset_sent.html"),name="password_reset_done",),
                  path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="../templates/registration/password_reset_form.html"),name="password_reset_confirm",),
                  path("reset_password_complete/",auth_views.PasswordResetCompleteView.as_view(template_name="../templates/registration/password_reset_complete.html"),
                        name="password_reset_complete",),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
