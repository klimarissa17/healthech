from django.contrib import admin
from .models import Drug, Patient, Doctor, Receipt, Disease, Day, PatientDisease, DrugByReceipt

# Register your models here.
admin.site.register(Drug)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Receipt)
admin.site.register(Disease)
admin.site.register(Day)
admin.site.register(PatientDisease)
admin.site.register(DrugByReceipt)
