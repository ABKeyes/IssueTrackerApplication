from django.contrib import admin

# Register your models here.

from .models import Project, ProjectUser

admin.site.register(Project)
admin.site.register(ProjectUser)
