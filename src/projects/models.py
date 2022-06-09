from enum import unique
import uuid
from django.db import models

from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Project(models.Model):
    user_max_length = 150
    project_max_length = 50

    id = models.UUIDField(
                        primary_key=True,
                        default = uuid.uuid4,
                        editable = False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=project_max_length)
    summary = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status= models.CharField(max_length=20, default="Open")

    def get_absolute_url(self):
        return reverse("projects:project-details", kwargs={"project_id": self.id})

    def get_update_url(self):
        return reverse("projects:project-update", kwargs={"project_id": self.id})

    def get_delete_url(self):
        return reverse("projects:project-delete", kwargs={"project_id": self.id})

    def get_issue_create_url(self):
        return reverse("projects:issues:issue-create", kwargs={"project_id": self.id})

    def get_add_user_url(self):
        return reverse("projects:project-add-user", kwargs={"project_id": self.id})


class ProjectUser(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def get_delete_url(self):
        return reverse("projects:project-remove-user", kwargs={"project_id": self.project.id,
                                                               "puser_id": self.id})