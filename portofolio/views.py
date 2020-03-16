from django.shortcuts import render
from .models import Project


def HomePage(request):
    projects = Project.objects.all()
    return render(request,"portofolio/index.html",{'projects': projects})
