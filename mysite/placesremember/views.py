from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'placesremember/index.html', {'title': 'Храните свои впечатления о посещённых местах'})

def addnew(request):
    return render(request, 'placesremember/addnew.html', {'title': 'У вас нет ни одного воспоминания'})
