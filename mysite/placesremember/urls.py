import oath as oath
from django.apps import config
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('placesremember', index, name='placesremember'),
    path('addnew/', addnew, name='addnew'),
    path('auth', autho, name='auth')

]