from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def portfolio(request):
    projects = Project.objects.all()
  

    return render(request, r"portfolio\projects.html", {"projects": projects})
