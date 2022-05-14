from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', loginRequest, name='loginRequest'),
    path('logout/', logoutRequest, name='logoutRequest')
]