# Create your views here.
from django.conf.urls import url
from simpleprojectmanagement import views

urlpatterns = [
    url(r'^$', views.index,  name="public_index"),
    url(r'^auth/login', views.login,  name="public_login"),
    url(r'^auth/register', views.register,  name="public_register"),

    #project urls this uses html based form
    url(r'^create_project', views.create_project, name="create_project"),
    url(r'^all_projects', views.get_all_projects, name="all_projects"),
    url(r'^project_detail/(?P<pk>[0-9]+)$', views.project_detail, name="project_detail"),
    url(r'^project_update/(?P<pk>[0-9]+)$', views.project_update, name="project_update"),
    url(r'^project_delete/(?P<pk>[0-9]+)$', views.project_delete, name="project_delete"),

    #this uses django based forms
]
