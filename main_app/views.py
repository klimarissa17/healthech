from django.shortcuts import render
from django.http import HttpResponse
from .models import Drugs


def index(request):
    return HttpResponse('heloworld')


def drugs_list(request):
    drugs = Drugs.objects.all()
    drugs = [d.get_name() for d in drugs]
    return render(request, 'main_app/drugs_list.html', {'drugs': drugs})
