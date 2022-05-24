from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "username"}))

    email = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "email"}))

    password1 = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "password"}))

    password2 = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "re-enter password"}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "username"}))
    password = forms.CharField(widget=forms.TextInput(
                                attrs={"placeholder": "password"}))

