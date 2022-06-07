from django import urls
from django.urls import path

from .views import (
    login_view,
    logoutUser,
    register_view,)

app_name='users'
urlpatterns=[

    path('login/', login_view, name='user-login'),
    path('register/', register_view, name='user-register'),
    path('logout/', logoutUser, name='user-logout')
    
    ]