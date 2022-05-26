from django.shortcuts import render
from .models import Project

from .forms import ProjectForm

# Create your views here.

def project_list_view(request):
    if request.user.is_authenticated:
        queryset = Project.objects.filter(user=request.user)
        context = {
            "project_list": queryset
            }
        return render(request, "projects/project_list.html", context)
    context = {}
    return render(request, "projects/project_list.html", context)

def project_create(request):

    form = ProjectForm(request.POST or None)
    context = { "form": form }

    if form.is_valid():
        user = request.user.username
        name = form.cleaned_data.get('name')
        print(f"Username: {user}")
        print(f"Project Name: {name}")


    return render(request, "projects/project_create.html", context)
