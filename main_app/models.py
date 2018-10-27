from django.db import models


# Create your models here.
class Drug(models.Model):
    name = models.TextField()
    active_substance = models.TextField()
    indications = models.TextField()
    contraindications = models.TextField()
    mode_of_application = models.TextField()


class Disease(models.Model):
    name = models.TextField()
    origin = models.TextField()
    forecast = models.TextField()
    drug_category = models.TextField()
    last_visit = models.DateTimeField()

class Patient(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    sex = models.TextField()
    specificities = models.TextField()


class Doctor(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    sex = models.TextField()
    specificities = models.TextField()


class Receipt(models.Model):
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    disease_id = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    is_critical = models.BooleanField()


class DrugsByReceipt(models.Model):
    receipt_id = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    drug_id = models.ForeignKey(Drugs, on_delete=models.CASCADE)


class PatientsDiseases(models.Model):
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    disease_id = models.ForeignKey(Diseases, on_delete=models.CASCADE)

