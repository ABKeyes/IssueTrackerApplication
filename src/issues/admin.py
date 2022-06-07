from django.contrib import admin

# Register your models here.

from .models import Comment, Issue

admin.site.register(Issue)
admin.site.register(Comment)