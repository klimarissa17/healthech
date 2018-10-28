from django.db import models


# Create your models here.
class Drug(models.Model):
    name = models.TextField()
    active_substance = models.TextField()
    indications = models.TextField()
    contraindications = models.TextField()
    mode_of_application = models.TextField(blank= True)

    def __str__(self):
        return str(self.name)


class Disease(models.Model):
    name = models.TextField()
    origin = models.TextField()
    forecast = models.TextField(blank= True)
    drug_category = models.TextField(blank= True)

    def __str__(self):
        return str(self.name)

class Patient(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    sex = models.TextField()
    specificities = models.TextField(blank= True)
    login = models.TextField(null= True, blank= True)
    def __str__(self):
        return str(self.name)


class Doctor(models.Model):
    name = models.TextField()
    expirience = models.SmallIntegerField(blank= True, null=True)
    specialty = models.TextField(blank= True)
    login = models.TextField(null=True, blank= True)
    def __str__(self):
        return str(self.name)


class Receipt(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease_id = models.ForeignKey(Disease, on_delete=models.CASCADE)
    is_critical = models.BooleanField()



class DrugByReceipt(models.Model):
    receipt_id = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)


class PatientDisease(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease_id = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def get_disease(self):
        return str(disease_id)
class Day(models.Model):
    date = models.DateField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    smile = models.IntegerField()
    
    def __str__(self):
        return str(self.date)

