from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^drugs_list/?$', views.drugs_list, name='drugs_list')
]