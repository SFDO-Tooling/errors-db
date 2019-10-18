from django.contrib import admin

from .models import User
from errors_db.api.models import ErrorInstance, Situation, Solution


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_active", "is_staff", "is_superuser", "date_joined")
    search_fields = ("username",)


@admin.register(ErrorInstance)
class ErrorInstanceAdmin(admin.ModelAdmin):
    list_display = ("message", "context", "created")
    list_filter = ["created"]


@admin.register(Situation)
class SituationAdmin(admin.ModelAdmin):
    list_display = ("error_msg", "context", "created")
    list_filter = ["created"]


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ("solution_type", "text", "situation", "created")
    list_filter = ["created"]

