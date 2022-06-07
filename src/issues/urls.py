from django.urls import path

from .views import (
    add_comment_view,
    add_tag_view,
    issue_create_view,
    issue_delete_view,
    issue_details_view,
    remove_tag,
)

app_name='issues'
urlpatterns=[
    path('create/', issue_create_view, name='issue-create'),
    path('<uuid:issue_id>', issue_details_view, name='issue-details'),
    path('<uuid:issue_id>/delete', issue_delete_view, name='issue-delete'),
    path('<uuid:issue_id>/addcomment', add_comment_view, name='issue-comment'),
    path('<uuid:issue_id>/addtag', add_tag_view, name='issue-tag'),
    path('<uuid:issue_id>/removetag/<int:tag_id>/', remove_tag, name='issue-tag-remove'),
    ]