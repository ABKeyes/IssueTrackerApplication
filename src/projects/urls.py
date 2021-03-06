from django.urls import path
from django.urls.conf import include


from .views import (
    project_add_user_view,
    project_create_view,
    project_delete_view,
    project_details_view,
    project_list_view,
    project_update_view,
    project_remove_user_view,
    )

app_name='projects'
urlpatterns=[
    path('', project_list_view, name='project-list'),
    path('create/', project_create_view, name='project-create'),
    path('<uuid:project_id>/', project_details_view, name='project-details'),
    path('<uuid:project_id>/update/', project_update_view, name='project-update'),
    path('<uuid:project_id>/delete', project_delete_view, name='project-delete'),
    path('<uuid:project_id>/issue/', include('issues.urls')),
    path('<uuid:project_id>/adduser/', project_add_user_view, name='project-add-user'),
    path('<uuid:project_id>/removeuser/<int:puser_id>', project_remove_user_view, name="project-remove-user"),
    ]