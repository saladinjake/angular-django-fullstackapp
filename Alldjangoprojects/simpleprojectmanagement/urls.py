# Create your views here.
from django.conf.urls import url
from simpleprojectmanagement import views

urlpatterns = [
    url(r'^home', views.index,  name="public_index"),
    url(r'^auth/login', views.login,  name="public_login"),
    url(r'^auth/register', views.register,  name="public_register"),

    #project urls
    url(r'^all_projects', views.get_all_projects, name="all_projects"),
    url(r'^project_detail-(?P<pk>\d+)', views.project_detail, name="project_detail"),
    url(r'^project_update-(?P<pk>\d+)', views.project_update name="project_update"),
    url(r'^project_delete-(?P<pk>\d+)', views.project_delete name="project_delete"),
]
