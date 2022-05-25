from django.shortcuts import render

# Create your views here.

def projects_list_view(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, "projects/project_list.html", context)
    context = {}
    return render(request, "projects/project_list.html", context)
