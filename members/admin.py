from django.contrib import admin
from .models import Group

@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):

    class Meta:
        model = Group
