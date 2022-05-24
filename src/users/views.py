from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, LoginUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


# Create your views here.


# View to handle user logins
def login_view(request):

    form = LoginUserForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data.get('username')
        print(username)
        password = form.cleaned_data.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("User is valid")
            login(request, user)
            return redirect('home')

        messages.error(request, "Username or password is incorrect")
        return render(request, "users/user_login.html", context)

    return render(request, "users/user_login.html", context)

# View to handle user registrations
def register_view(request):
    form = CreateUserForm(request.POST or None)

    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        return redirect('users:user-login')

    context = {"form": form}

    return render(request, "users/user_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect('users:user-login')
