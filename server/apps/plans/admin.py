from django.contrib import admin

from server.apps.plans.models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["name", "thumbnail_sizes", "original_link", "expiring_link"]
