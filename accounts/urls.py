from django.contrib.auth import views as auth_views
from django.urls import path

app_name = "accounts"
urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="../templates/registration/password_reset.html"),
        name="reset_password",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="../templates/registration/password_reset_sent.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="../templates/registration/password_reset_form.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="../templates/registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
