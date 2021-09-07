from django.urls import path

from users import views as user_views

app_name = "users"

urlpatterns = [
    path("profile/dge<id>du/", user_views.profile_page, name="user_profile"),
    path("organization/", user_views.organization_page),
    path("accounts/logout/", user_views.logout_view, name="logout"),
    path("profile/dge<id>du/editor/", user_views.profile_editor, name="profile_redactor"),
]
