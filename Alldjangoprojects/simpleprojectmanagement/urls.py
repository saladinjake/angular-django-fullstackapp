# Create your views here.
from django.conf.urls import url
from simpleprojectmanagement import views

urlpatterns = [
    url(r'^', views.index),

]
