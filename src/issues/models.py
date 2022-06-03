from django.db import models
import uuid
from django.db import models
from projects.models import Project

from django.urls import reverse

# Create your models here.

class Issue(models.Model):
    id = models.UUIDField(
                        primary_key=True,
                        default= uuid.uuid4,
                        editable=False)
    issueName = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=False)
    status = models.CharField(max_length=20, default="Open")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("projects:issues:issue-details", kwargs={
                                                            "project_id": self.project.id, 
                                                            "issue_id": self.id})
    def get_project_url(self):
        return reverse("projects:project-details", kwargs={
                                                        "project_id": self.project.id})

class IssueComment(models.Model):
    description = models.TextField(max_length=200, blank=False)
    timecreated = models.DateTimeField(auto_now=False, auto_now_add=True)
