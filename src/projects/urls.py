from django.urls import path


from .views import (
    project_create,
    project_list_view,
    )

app_name='projects'
urlpatterns=[
    path('', project_list_view, name='project-list'),
    path('create/', project_create, name='project-create'),
    ]