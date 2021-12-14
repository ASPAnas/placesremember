from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'placesremember/index.html')

def noone(request):
    return HttpResponse("У вас нет ни одного воспоминания")
