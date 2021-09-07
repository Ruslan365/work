from django.contrib import admin
from .models import User, SocialMedia


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "last_login_at",
    ]
    readonly_fields = ("password", "created_at", "last_login_at")

# admin.register(SocialMedia)