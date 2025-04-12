
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
import temperatura.views as views

urlpatterns = ([
    path('<int:id>', views.getTemperatura, name='temperatura'),
    path('', views.getTemperatura, name='temperatura'),
])
