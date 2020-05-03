from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('produtos_demanda/', produtos_demanda, name='produtos_demanda'),
]