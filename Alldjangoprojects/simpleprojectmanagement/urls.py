# Create your views here.
from django.conf.urls import url
from simpleprojectmanagement import views

urlpatterns = [
    url(r'^home', views.index,  name="public_index"),
    url(r'^auth/login', views.login,  name="public_login"),
    url(r'^auth/register', views.register,  name="public_register"),

]
