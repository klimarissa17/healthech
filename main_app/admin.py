from django.contrib import admin
from .models import Drug, Patient, Doctor

# Register your models here.
admin.site.register(Drug)
admin.site.register(Patient)
admin.site.register(Doctor)
