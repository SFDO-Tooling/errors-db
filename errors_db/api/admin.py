from django.contrib import admin

from .models import User
from errors_db.api.models import ErrorInstance


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_active", "is_staff", "is_superuser", "date_joined")
    search_fields = ("username",)


@admin.register(ErrorInstance)
class ErrorInstanceAdmin(admin.ModelAdmin):
    list_display = ("message", "context", "created")
    list_filter = ["created"]

