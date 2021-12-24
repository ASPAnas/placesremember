from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'placesremember/index.html')

def outh(request):
    return render(request, 'placesremember/config.php')

def addnew(request):
    return render(request, 'placesremember/addnew.html', {'title': 'У вас нет ни одного воспоминания'})
