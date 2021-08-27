from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "last_login_at",
    ]
    readonly_fields = ("password", "created_at", "last_login_at")
