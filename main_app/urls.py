from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='hello'),
    url(r'drugs_list', views.drugs_list, name='drugs_list')
]