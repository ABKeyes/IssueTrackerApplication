from django.shortcuts import get_object_or_404, redirect, render

from issues.models import Issue
from .models import Project

from django.contrib.auth.decorators import login_required

from django.contrib import messages

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

def check_ownership(obj, request):
    print("Checking ownership")
    print(obj.user)
    print(request.user)
    if obj.user == request.user:
        return True
    print("User is not the owner of this project,")
    return False

@login_required()
def project_create_view(request):

    form = ProjectForm(request.POST or None)
    
    # Check if form is filled out.
    if form.is_valid():

        newname = form.cleaned_data.get('name')
        if Project.objects.filter(user=request.user, name=newname).exists():
            messages.error(request, "Project name already in use.")
            context = { "form": form }
            return render(request, "projects/project_create.html", context)

        # Save form entries into project
        project = form.save(commit=False)

        # Add current user as user for project
        project.user = request.user
        project.save()
        form = ProjectForm()
        return redirect('projects:project-list')
         
    context = { "form": form }

    return render(request, "projects/project_create.html", context)

def project_update_view(request, project_id):

    obj = get_object_or_404(Project, id=project_id)
    
    if check_ownership(obj, request) == False:
        return redirect('home')

    form = ProjectForm(request.POST or None, instance=obj)
    context = { 
        "form": form ,
        "update": True}

    if form.is_valid():
        if 'name' in form.changed_data:
            newname = form.cleaned_data.get('name')
            if Project.objects.filter(user=request.user, name=newname).exists():
                messages.error(request, "Project name already in use.")
                context = { 
                "form": form ,
                "update": True}
                return render(request, "projects/project_create.html", context)
        form.save()
        return redirect(obj.get_absolute_url())

    return render(request, "projects/project_create.html", context)

@login_required()
def project_details_view(request, project_id):

    obj = get_object_or_404(Project, id=project_id)
    
    if not check_ownership(obj, request):
        return redirect('home')

    issueset = Issue.objects.filter(project=obj).order_by('-status')

    context = {
        "project": obj,
        "issueset": issueset,
        }

    print(issueset.count())

    return render(request, "projects/project_details.html", context)


@login_required()
def project_delete_view(request, project_id):

    obj = get_object_or_404(Project, id=project_id)

    if check_ownership(obj, request) == False:
        return redirect('home')

    if request.method == "POST":
        print("Deleteing")
        print(obj)
        obj.delete()
        return redirect('projects:project-list')
    context = {
        "project": obj
        }
    return render(request, "projects/project_delete.html", context)