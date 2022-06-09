from django.shortcuts import get_object_or_404, redirect, render

from issues.models import Issue, Tag
from .models import Project, ProjectUser

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import ProjectForm, ProjectUserForm

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

# View to display all projects that they own and are a part of.
def project_list_view(request):
    if request.user.is_authenticated:
        queryset = Project.objects.filter(user=request.user)
        membershipset = ProjectUser.objects.filter(user=request.user)
        print(membershipset)
        context = {
            "project_list": queryset,
            "membershipset": membershipset,
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

def check_membership(obj, request):
    if ProjectUser.objects.get(project=obj, user=request.user):
        print(f"{request.user.username} is a member")
        return True
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
    
    if not check_ownership(obj, request):
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

    users = ProjectUser.objects.filter(project=obj)
    print(users)

    owner = check_ownership(obj, request)
    
    if (not owner) and (not check_membership(obj, request)):

        return redirect('home')

    issueset = Issue.objects.filter(project=obj).order_by('-status')
    tags = Tag.objects.filter(issue__in=issueset)

    context = {
        "project": obj,
        "issueset": issueset,
        "users": users,
        "tags": tags,
        "owner": True,
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

def project_add_user_view(request, project_id):
    obj = get_object_or_404(Project, id=project_id)
    

    if check_ownership(obj, request) == False:
        return redirect(obj.get_absolute_url())

    form = ProjectUserForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        user = User.objects.get(username=username)
        print(user)
        if user is None:
            messages.error(request, "There is no user by that username.")
            context = {
                "project": obj,
                "form": form,
                }
            return render(request, "projects/project_add_user.html", context)

        projectuser = ProjectUser()
        projectuser.project = obj
        projectuser.user = user
        projectuser.save()
        return redirect(obj.get_absolute_url())

    context = {
        "project": obj,
        "form": form,
        }
    return render(request, "projects/project_add_user.html", context)

def project_remove_user_view(request, project_id, puser_id):

    project = get_object_or_404(Project, id=project_id)
    projectuser = get_object_or_404(ProjectUser, id=puser_id)

    if check_ownership(project, request) == False:
        return redirect(project.get_absolute_url())

    if request.method == "POST":
        print("Removing user from project")
        print(projectuser.user.username)
        projectuser.delete()
        return redirect(project.get_absolute_url())

    context = {
        "project": project,
        "user": projectuser,
        }

    return render(request, "projects/project_remove_user.html", context)