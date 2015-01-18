from django.shortcuts import render_to_response
from django.views.generic import ListView
from .models import Project


class ProjectsListView(ListView):
    model = Project
    template_name = 'portfolio/main.html'
    context_object_name = 'projects'

