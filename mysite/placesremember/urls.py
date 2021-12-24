import oath as oath
from django.apps import config
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('', outh, name='home'),
    path('addnew/', addnew, name='addnew'),
]

