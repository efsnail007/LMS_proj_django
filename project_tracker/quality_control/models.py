from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    STATUS_CHOICES = [
        ("New", "Новая"),
        ("In_progress", "В работе"),
        ("Completed", "Завершена"),
    ]
    PRIORITY_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="bug_reports"
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        related_name="bug_reports",
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="New")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ("Consideration", "Рассмотрение"),
        ("Accepted", "Принято"),
        ("Rejected", "Отклонено"),
    ]
    PRIORITY_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="feature_requests"
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        related_name="feature_requests",
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="Consideration"
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
