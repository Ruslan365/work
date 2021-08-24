from django.contrib import admin
from .models import User, SocialNetwork, Role


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "last_login_at",
    ]
    readonly_fields = ("password", "created_at", "last_login_at")


admin.site.register(SocialNetwork)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

    class Meta:
        model = Role
