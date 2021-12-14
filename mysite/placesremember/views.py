from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Храните свои воспоминания о посещенных местах")

def noone(request):
    return HttpResponse("У вас нет ни одного воспоминания")
