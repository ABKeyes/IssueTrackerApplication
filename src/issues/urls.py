from djagno.urls import path

app_name='issues'

urlpatterns=[
    path('create/', issue_create_role, name='issue-create'),
    #path('<uuid:issue_id>/')
    ]