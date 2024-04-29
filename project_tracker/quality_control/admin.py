from django.contrib import admin

from .models import BugReport, FeatureRequest


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project",
        "task",
        "status",
        "priority",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "priority", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_editable = ("status",)
    fieldsets = [
        (
            "Основная информация",
            {
                "fields": [
                    "title",
                    "description",
                    "project",
                    "task",
                    "status",
                    "priority",
                ]
            },
        ),
    ]


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project",
        "task",
        "status",
        "priority",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "priority", "created_at", "updated_at")
    search_fields = ("title", "description")
    fieldsets = [
        (
            "Основная информация",
            {
                "fields": [
                    "title",
                    "description",
                    "project",
                    "task",
                    "status",
                    "priority",
                ]
            },
        ),
    ]
