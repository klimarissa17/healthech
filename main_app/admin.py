from django.contrib import admin
from .models import Drugs, Patients, Doctors

# Register your models here.
admin.site.register(Drugs)
admin.site.register(Patients)
admin.site.register(Doctors)
