# Create your views here.
from django.conf.urls import url
from learning import views

urlpatterns = [
    url(r'^api/tutorials$', views.post_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.post_detail),
    url(r'^api/tutorials/published$', views.post_list_published)
]
