from django.contrib import admin
from .models import User, Work


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    class Meta:
        model = Work
