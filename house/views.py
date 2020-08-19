from django.shortcuts import render

from .models import *

def list_bulidings(request):
    buildings = Building.objects.all()
    context = {'buildings':buildings}

    return render(request,'house/buildings.html', context)

def list_house(request):
    houses = House.objects.all()
    context = {'houses':houses}

    return render(request,'house/houses.html', context)

def list_teneant(request):
    teneants = Teneant.objects.all()
    context = {'teneants':teneants}

    return render(request, 'house/teneants.html', context)