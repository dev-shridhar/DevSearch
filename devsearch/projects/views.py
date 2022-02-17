from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    return render(request, 'projects/projects.html', {'projects': Project.objects.all()})


def theproject(request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectobj, 'tags': tags } )


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
         form = ProjectForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance = project)
    
    if request.method == 'POST':
        form = ProjectForm(instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_object.html', context)



