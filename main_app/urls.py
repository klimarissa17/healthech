from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/?$', views.home, name='home'),
    url(r'^drugs_list/?$', views.drugs_list, name='drugs_list'),
    url(r'^patient_home/?$', views.patient_home, name='patient_home'),
    url(r'^doctor_home/?$', views.doctor_home, name='doctor_home')
]
