from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from simpleprojectmanagement.models import Project,Developer,Supervisor, UserProfile, Task

"""
 guest and auth pages
"""

def index(request):
    return render(request, 'public/index.html')

def login(request):
    return render(request, 'public/login.html')

def register(request):
    return render(request, 'public/register.html')

'''
 project crud operations
'''

def create_project(request):
     if request.POST:
         if 'title' in request.POST:
             title = request.POST.get('title', '')
         else:
             error=True
         if 'description' in request.POST:
             description = request.POST.get('description', '')
         else:
             error=True
         if 'client_name' in request.POST:
             client_name = request.POST.get('client_name', '')
         else:
             error=True
         if not error:
             new_project = Project(title=title, description=description,client_name=client_name) # line 2
             new_project.save() # line 3
             return render(request, 'public/create_project.html', {'action':'Save successful'})
         else:
            return render(request, 'public/create_project.html', {'action':'Error in form'})
     else:
          return render(request, 'public/create_project.html', {'action':'Add a project'})

def get_all_projects(request):
    all_projects = Project.objects.all()
    return render(request, 'public/all_projects.html', {'message': "All projects", 'all_projects': all_projects})

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'public/project_detail.html', {'project' : project})

def project_update(request,pk):
    project = Project.objects.get(id=pk)
    project.title = request.POST.get("title", project.title)
    project.description = request.POST.get("title", project.title)
    project.client_name = request.POST.get("title", project.title)
    project.id = request.get("title", pk)
    return render(request, 'public/project_update.html', {'project' : project})

def project_delete(request,pk):
    project = Project.objects.get(id = 1)
    project.delete() # line 1

    return render(request, 'public/project_detail.html', {'action' : 'Delete was successful'})

def project_flush(request):
    all_tasks = Task.objects.all()
    all_tasks.delete() # line 2
    return render(request, 'public/project_detail.html', {'action' : 'Delete tasks'})


'''
 developer crud operations
'''





'''
 supervisor crud operations
'''




'''
 user crud operations
'''



'''
 task crud operations
'''
