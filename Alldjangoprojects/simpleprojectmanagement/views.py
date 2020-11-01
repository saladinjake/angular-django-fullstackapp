from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from simpleprojectmanagement.models import Project,Developer,Supervisor, UserProfile, Task

# now lets import the django forms
from  simpleprojectmanagement.forms.generic import NewUserForm, NewDeveloperForm, NewSupervisorForm, EditDeveloperForm, EditUserForm, EditSupervisorForm
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
 1 project crud operations basics with html based forms
'''
def create_project(request):
     title = description = client_name = error = None
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
    project.id = request.POST.get("title", pk)
    title = description = client_name = error = None

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
            project.title = request.POST.get("title")
            project.description = request.POST.get("description")
            project.client_name = request.POST.get("title")
            project.id =  pk
            project.save()
            return HttpResponseRedirect(reverse('all_projects'))
        else:
            return render(request, 'public/project_update.html', locals())
    else:
        return render(request, 'public/project_update.html', locals())

def project_delete(request,pk):
    project = Project.objects.get(id = pk)
    project.delete() # line 1

    return HttpResponseRedirect(reverse('all_projects'))

def project_flush(request):
    all_tasks = Task.objects.all()
    all_tasks.delete() # line 2
    return HttpResponseRedirect(reverse('all_projects'))




'''
 2 developer crud operations with django forms.Form
'''

def create_developer(request):
    if request.POST:
        form  = NewDeveloperForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            age = form.cleaned_data['age']
            last_login = form.cleaned_data['last_login']
            email = form.cleaned_data['email']
            experience_role = form.cleaned_data['experience_role']
            date_created = form.cleaned_data['date_created']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            supervisedby = form.cleaned_data['supervisedby']
            new_developer = Developer(
            username=username,email=email,password=password,
            phone=phone, age =age,last_login=last_login,date_created =date_created,
            experience_role=experience_role ,
            supervisedby=supervisedby
            )
            new_developer.save()
            return render(request,'public/djangoformbuilder/create_developer.html',{'form': form, 'success':True})
        else:
            return render(request,'public/djangoformbuilder/create_developer.html',{'form': form, 'error':True})
    else:
        form  = NewDeveloperForm(request.POST)
        return render(request,'public/djangoformbuilder/create_developer.html',{'form': form})


def get_all_developers(request):
    all_developers = Developer.objects.all()
    return render(request, 'public/all_developers.html', {'message': "All projects", 'all_developers': all_developers})


def developer_detail(request,pk):
    developer = Developer.objects.get(id=pk)
    return render(request, 'public/developer_detail.html', {'developer' : developer})

def developer_update(request,pk):
    '''This time i am using django forms not html forms '''
    developer = Developer.objects.get(id=pk)
    initialValues ={
      'username':developer.username,
      'email':developer.email,
      'password':developer.password,
      'phone':developer.phone,
      'age' :developer.age,
      'last_login':developer.last_login,
      'date_created' :developer.date_created,
      'experience_role':developer.experience_role ,
      'supervisedby':developer.supervisedby

    }
    error = success = None
    form = EditDeveloperForm(initial=initialValues)
    #now if there is a post for update
    if request.POST:
        form  = EditDeveloperForm(request.POST)
        if form.is_valid():
            developer.phone = form.cleaned_data['phone']
            developer.age = form.cleaned_data['age']
            developer.last_login = form.cleaned_data['last_login']
            developer.email = form.cleaned_data['email']
            developer.experience_role = form.cleaned_data['experience_role']
            developer.date_created = form.cleaned_data['date_created']
            developer.username = form.cleaned_data['username']
            developer.password = form.cleaned_data['password']
            developer.supervisedby = form.cleaned_data['supervisedby']

            developer.save()
            return render(request,'public/djangoformbuilder/developer_update.html',{'form': form, 'success':True})
        else:
            return render(request,'public/djangoformbuilder/developer_update.html',{'form': form, 'error':True})
    else:
        form  = EditDeveloperForm(initial=initialValues)
        return render(request,'public/djangoformbuilder/developer_update.html',{'form': form}) #initial

    return render(request, 'public/djangoformbuilder/developer_update.html', {"form": form}) #initial form


def developer_delete(request):
    developer = Developer.objects.get(id = pk)

    developer.delete() # line 1
    return HttpResponseRedirect(reverse('all_developers'))

'''
 3 supervisor crud operations django forms.ModelForm and cbvs
'''




'''
 4 user crud operations using cbvs
'''



'''
 5 task crud operations
'''
