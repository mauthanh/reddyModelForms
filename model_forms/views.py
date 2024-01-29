from django.shortcuts import render

from model_forms.models import Project
from model_forms.forms import ProjectForm


# Create your views here.
def index(request):
    return render(request, 'model_forms/index.html')


def list_projects(request):
    projects = Project.objects.all()
    return render(request, 'model_forms/list.html',
                  {'projects': projects})
