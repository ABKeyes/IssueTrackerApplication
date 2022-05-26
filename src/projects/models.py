from enum import unique
from django.db import models

# Create your models here.

class Project(models.Model):
    user_max_length = 150
    project_max_length = 50

    user = models.CharField(max_length=user_max_length)
    name = models.CharField(max_length=project_max_length)
    summary = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    #def get_absolute_url(self):
    #    return reverse("project")