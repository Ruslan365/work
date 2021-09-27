from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    model = User

    fieldsets = ((None, {'fields': ('avatar','first_name', 'last_name',
                                    'email', 'password', 'about',
                                    'birth_date', 'twitter_id', 'facebook_id',
                                    'role', 'last_login_at', 'created_at',
                                    )}),)

    # add_fieldsets = ((None, {'fields': ('name', 'image',)}),)

    list_display = [
        "email",
        "last_login_at",
    ]
    readonly_fields = ("password", "created_at", "last_login_at")
