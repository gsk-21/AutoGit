import json
from .models import Project
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.dateparse import parse_date


def home(request):
    return render(request, 'home.html')


def add_project(request):
    result = ''
    title = request.POST.get('title')
    directory = request.POST.get('directory')
    branch_name = request.POST.get('branch_name')
    default = request.POST.get('default')

    print(title, "\t", directory, "\t", branch_name, "\t", default)

    project = Project()
    project.title = title
    project.directory = directory
    project.branch_name = branch_name
    project.default = bool(default)

    project.save()
    result = 'Project added'

    return HttpResponse(
        json.dumps({'result': result}),
        content_type="application/json"
    )
