from django.urls import path

from .views import (
    issue_create_view,
    issue_details_view,
)

app_name='issues'
urlpatterns=[
    path('create/', issue_create_view, name='issue-create'),
    path('<uuid:issue_id>', issue_details_view, name='issue-details'),
    ]