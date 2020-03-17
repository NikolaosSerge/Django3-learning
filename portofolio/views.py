from django.shortcuts import render, get_object_or_404
from .models import Project


def HomePage(request):
    projects = Project.objects.all()
    return render(request,"portofolio/index.html",{'projects': projects})


def detail(request, project_id):
    project = get_object_or_404(Project,pk=project_id)
    return render(request,'portofolio/detail.html',{'project':project})
