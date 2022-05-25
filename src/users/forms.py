from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "username",
                                       "height": "50px",
                                       "class": "user-fields"}))

    email = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "email",
                                       "class": "user-fields"}))

    password1 = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "password",
                                       "class": "user-fields"}))

    password2 = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "re-enter password",
                                       "class": "user-fields"}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "username",
                                       "class": "user-fields"}))
    password = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "password",
                                       "class": "user-fields"}))

