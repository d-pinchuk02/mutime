from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Project, TimeEntry


class ProjectAdmin(ModelAdmin):
    list_display = ("title", "created_at")
    readonly_fields = ("created_at", "updated_at")


class TimeEntryAdmin(ModelAdmin):
    list_display = ("title", "project", "started_at", "stopped_at")
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Project, ProjectAdmin)
admin.site.register(TimeEntry, TimeEntryAdmin)
