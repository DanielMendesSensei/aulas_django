from django.contrib import admin
from django.urls import path
from . import views

app_name = 'iFood'

urlpatterns = [
    path('', views.home, name='home'),
]