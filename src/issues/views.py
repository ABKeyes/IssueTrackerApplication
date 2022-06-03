from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateIssueForm, UpdateIssueForm

from .models import Issue

from projects.models import Project

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

@login_required()
def issue_create_view(request, project_id):
    form = CreateIssueForm(request.POST or None)

    if form.is_valid():
        print("Issue is valid")
        print(form.cleaned_data)

        issueName = form.cleaned_data.get('issueName')

        print(project_id)
        project = get_object_or_404(Project, id=project_id)
        print(project)

        if Issue.objects.filter(project = project, issueName = issueName).exists():
            messages.error(request, "Issue name already in use")
            context = {"form": form}
            return render(request, "issues/issue_create.html", context)

        issue = form.save(commit=False)

        issue.project = project
        issue.save()
        form = CreateIssueForm
        return redirect('../../')

    context = {"form": form}

    return render(request, "issues/issue_create.html", context)

@login_required()
def issue_details_view(request, project_id, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    form = UpdateIssueForm(request.POST or None, instance=issue)

    for field in form:
        print("Field Error:", field.name,  field.errors)

    if form.is_valid():
        print(form.cleaned_data)
        print("Updating issue")
        form.save()

    context = {
        "form": form,
        "issue": issue,
        }

    return render(request, "issues/issue_details.html", context)

