from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'placesremember/index.html')

def autho(request):
    return render(request, 'api.vkontakte.ru/oauth/authorize?client_id=8034656&scope=&redirect_uri=http://127.0.0.1:80/placesremember&response_type=code')

def addnew(request):
    return render(request, 'placesremember/addnew.html', {'title': 'У вас нет ни одного воспоминания'})
