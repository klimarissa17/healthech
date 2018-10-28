from django.shortcuts import render
from django.http import HttpResponse
from .models import Drug, Disease, Patient, Doctor, PatientDisease, Day, Receipt, DrugByReceipt
from django.forms.models import model_to_dict
import datetime
from django.utils import timezone
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html')
    elif ('Doctors',) in request.user.groups.values_list('name'):
        return doctor_home(request)
    elif ('Patients',) in request.user.groups.values_list('name'):
        patient_home(request)
        return patient_home(request)
    return HttpResponse('You\'re neither a doctor nor a patient!')

def doctor_home(request): 
    user = request.user
    doctor = Doctor.objects.get(login= user)
    name = doctor.name
    patients = Patient.objects.all()
    patients = [str(p) for p in patients]
    return render(request, 'main_app/doctor_home.html', {  })

def patient_home(request):
    #print(request.user)
    user = request.user
    patient_obj = Patient.objects.get(login= user)
    patient = model_to_dict(patient_obj)
    name = patient['name']
    print(name)
    id = patient['id']
    qs = PatientDisease.objects.filter(patient_id = id)
    diagnosises_list = [model_to_dict(d)['disease_id'] for d in qs]
    diagnosis = [str(Disease.objects.get(id= i)) for i in diagnosises_list][0]
    disease_id = diagnosises_list[0] 
    print(disease_id)
    receipt_obj = Receipt.objects.get(disease_id= disease_id, patient_id= id)
    print(receipt_obj)
    receipt = model_to_dict(receipt_obj)['id']
    print(receipt)
    drug_obj = DrugByReceipt.objects.get(receipt_id= receipt)
    drug_id = model_to_dict(drug_obj)['drug_id']
    drug = model_to_dict(Drug.objects.get(id= drug_id))['name']
    drug_info = model_to_dict(Drug.objects.get(id= drug_id))['mode_of_application']
    info1 = 'lorem ipsum dolor'
     
    print(diagnosis)
    # today = datetime.date.now()
    # today = timezone.now()
    today = datetime.datetime.now().date()
    print(today)
    try:
        smile = model_to_dict(Day.objects.get(date= today, patient_id= id))['smile']
    except Day.DoesNotExist:
        smile = None
    return render(request, 'main_app/patient_home.html', {'name': name,'disease': diagnosis,  'name_of_med': drug, 'prescription':drug_info, 'disease_info': info1 })


def drugs_list(request):
    drugs = Drug.objects.all()
    drugs = [str(d) for d in drugs]
    return render(request, 'main_app/drugs_list.html', {'drugs': drugs})



