import json
from .models import Project, DefaultProject
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .git_automation import Git
from django.utils import timezone

# Create your views here.
from django.utils.dateparse import parse_date, parse_time


def home(request):
    context = dict()
    projects = Project.objects.all()
    context['projects'] = projects
    return render(request, 'home.html', context)


def add_project(request):
    if request.method == 'POST':

        result = ''
        title = request.POST.get('title')
        directory = request.POST.get('directory')
        branch_name = request.POST.get('branch_name')
        default = request.POST.get('default')

        if str(default).lower() == 'true':
            default = True
        elif str(default).lower() == 'false':
            default = False

        if default:
            set_default_project(title, directory, branch_name)

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
    else:
        return render(request, 'add_project.html')


def edit_project(request, id):
    if request.method == 'POST':
        return HttpResponse("Invalid request")
    else:
        print("ID:", id)
        context = dict()
        project = Project.objects.get(id=id)
        if not project.autocommit:
            project.autocommit = ""
        if not project.default:
            project.default = ""
        context['project'] = project
        return render(request, 'edit_project.html', context)


def update_project(request):
    if request.method == 'POST':
        result = ''
        project_id = request.POST.get('project_id')
        title = request.POST.get('title')
        directory = request.POST.get('directory')
        branch_name = request.POST.get('branch_name')
        default = request.POST.get('default')
        autocommit = request.POST.get('autocommit')
        autocommit_time_str = request.POST.get('autocommit_time')

        if str(default).lower() == 'true':
            default = True
        elif str(default).lower() == 'false':
            default = False

        if str(autocommit).lower() == 'true':
            autocommit = True
        elif str(autocommit).lower() == 'false':
            autocommit = False

        if default:
            set_default_project(title, directory, branch_name)
        project = Project.objects.get(id=project_id)
        project.title = title
        project.directory = directory
        project.branch_name = branch_name
        project.default = default
        project.autocommit = autocommit
        project.save()
        result = 'Project Updated'

        return HttpResponse(
            json.dumps({'result': result}),
            content_type="application/json"
        )

    else:
        return HttpResponse("Invalid request")


def run_git(request):
    if request.method == 'POST':
        result = dict
        default_project = DefaultProject.objects.get(id=1)
        title = default_project.title
        directory = default_project.directory

        command = request.POST.get('command')
        print("Command from front-end:",command)

        commands = str(command).split(' ')
        git = Git(project_directory=directory)
        response = git.run_process(command=commands)
        print(response)
        exit_code = response['exit_code']
        stdout = response['stdout']
        stderr = response['stderr']

        return HttpResponse(
            json.dumps({
                'exit_code': exit_code,
                'stdout': stdout,
                'stderr': stderr
            }),
            content_type="application/json"
        )

    else:
        return HttpResponse("Invalid request")


def set_default_project(title, directory, branch_name):
    projects = Project.objects.all()
    for project in projects:
        project.default = False
        project.save()
    default_project = DefaultProject.objects.get(id=1)
    default_project.title = title
    default_project.directory = directory
    default_project.branch_name = branch_name
    default_project.save()
