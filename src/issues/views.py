from django.shortcuts import get_object_or_404, redirect, render

from projects.views import check_ownership
from .forms import CreateIssueForm, CreateTagForm, UpdateIssueForm, CreateCommentForm

from .models import Issue, Comment, Tag

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
        return redirect(issue.get_project_url())

    context = {"form": form}

    return render(request, "issues/issue_create.html", context)

def remove_tag(request, project_id, issue_id, tag_id):
    issue = get_object_or_404(Issue, id=issue_id)
    tag = get_object_or_404(Tag, issue=issue, id=tag_id)
    tag.delete()
    return redirect(issue.get_absolute_url())

@login_required()
def issue_details_view(request, project_id, issue_id):

    issue = get_object_or_404(Issue, id=issue_id)
    form = UpdateIssueForm(request.POST or None, instance=issue)
    comments = Comment.objects.filter(issue=issue).order_by('-timecreated')
    tags = Tag.objects.filter(issue=issue)


    for field in form:
        print("Field Error:", field.name,  field.errors)

    if form.is_valid():
        print(form.cleaned_data)
        print("Updating issue")
        form.save()

        return redirect(issue.get_project_url())

    context = {
        "form": form,
        "issue": issue,
        "comments": comments,
        "tags": tags,
        }

    return render(request, "issues/issue_details.html", context)


@login_required()
def issue_delete_view(request, project_id, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    
    if check_ownership(issue.project, request) == False:
        return redirect(issue.get_absolute_url)

    if request.method == "POST":
        print("Deleting")
        print(issue)
        project = issue.project
        issue.delete()
        return redirect(project.get_absolute_url())

    context = {
        "issue": issue
        }
    return render(request, "issues/issue_delete.html", context)

@login_required()
def add_comment_view(request, project_id, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)

    form = CreateCommentForm(request.POST or None)

    context = {
        "issue": issue,
        "form": form,
        }

    if form.is_valid():
        comment = form.save(commit=False)

        comment.issue = issue
        comment.save()
        form = CreateIssueForm()
        return redirect(issue.get_absolute_url())

    

    return render(request, "issues/comment_add.html", context)

@login_required()
def add_tag_view(request, project_id, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    form = CreateTagForm(request.POST or None)

    context = {
        "issue": issue,
        "form": form,
        }

    if form.is_valid():
        tag = form.save(commit=False)

        tag.issue = issue
        tag.save()
        form = CreateTagForm()
        return redirect(issue.get_absolute_url())
    
    return render(request, "issues/tag_add.html", context)