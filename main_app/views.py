from django.shortcuts import render
from django.http import HttpResponse
from .models import Drug


def home(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html')
    elif ('Doctors',) in request.user.groups.values_list('name'):
        return doctor_home(request)
    elif ('Patients',) in request.user.groups.values_list('name'):
        return patient_home(request)
    return HttpResponse('You\'re neither a doctor nor a patient!')

def doctor_home(request):
    return render(request, 'main_app/doctor_home.html', {  })

def patient_home(request):
    return render(request, 'main_app/patient_home.html', {})


def drugs_list(request):
    drugs = Drug.objects.all()
    drugs = [str(d) for d in drugs]
    return render(request, 'main_app/drugs_list.html', {'drugs': drugs})
