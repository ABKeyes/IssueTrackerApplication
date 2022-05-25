from django.urls import path


from .views import (
    projects_list_view,
    )

app_name='projects'
urlpatterns=[
    path('', projects_list_view, name='projects-list'),
    ]