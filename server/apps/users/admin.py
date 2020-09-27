from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from server.apps.users.models import Plan, User


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["name", "thumbnail_sizes", "original_link", "expiring_link"]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = BaseUserAdmin.list_display + ("plan",)

    def get_fieldsets(self, request, obj=None):
        fieldsets = list(super(UserAdmin, self).get_fieldsets(request, obj))
        fieldsets.insert(2, (_("Plan"), {"fields": ("plan",)}))
        return fieldsets
