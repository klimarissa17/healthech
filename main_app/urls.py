from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.home, name='home'),
<<<<<<< HEAD
    url(r'^drugs_list/?$', views.drugs_list, name='drugs_list')
=======
    url(r'^home/?$', views.home, name='home'),
    url(r'^drugs_list/?$', views.drugs_list, name='drugs_list'),
>>>>>>> 9ad06c43e088739c7e10b2a397c9abb1d1c468c1
]
