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

    def get_tags(self):
        print("getting tags")
        return Tag.objects.filter(issue=self)
    
    def get_absolute_url(self):
        return reverse("projects:issues:issue-details", kwargs={
                                                            "project_id": self.project.id, 
                                                            "issue_id": self.id})
    def get_delete_url(self):
        return reverse("projects:issues:issue-delete", kwargs={
                                                        "project_id": self.project.id,
                                                        "issue_id": self.id})
    def get_project_url(self):
        return reverse("projects:project-details", kwargs={
                                                        "project_id": self.project.id})
    def get_comment_create_url(self):
        return reverse("projects:issues:issue-comment", kwargs={
                                                            "project_id": self.project.id, 
                                                            "issue_id": self.id})
    def get_add_tag(self):
        return reverse("projects:issues:issue-tag", kwargs={
                                                            "project_id": self.project.id, 
                                                            "issue_id": self.id})
    

class Comment(models.Model):
    description = models.TextField(max_length=200, blank=False)
    timecreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=20, blank=False)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    def get_delete_tag_url(self):
        return reverse("projects:issues:issue-tag-remove", kwargs={
                                                            "project_id": self.issue.project.id, 
                                                            "issue_id": self.issue.id,
                                                            "tag_id": self.id})