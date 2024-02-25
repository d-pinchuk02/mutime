from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default="#0918e6")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TimeEntry(models.Model):
    title = models.TextField(max_length=1024)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True)
    started_at = models.DateTimeField(auto_now=True)
    stopped_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
