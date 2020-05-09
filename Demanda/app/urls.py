from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('produtos_demanda/', produtos_demanda, name='produtos_demanda'),
    path('produtos_demanda/<int:id>', delete_produto, name='delete_produto'),
]