from django.shortcuts import render
from django.http import HttpResponse
from .models import Drug


def home(request):
    return HttpResponse('hello')


def drugs_list(request):
    drugs = Drug.objects.all()
    drugs = [d.get_name() for d in drugs]
    return render(request, 'main_app/drugs_list.html', {'drugs': drugs})
