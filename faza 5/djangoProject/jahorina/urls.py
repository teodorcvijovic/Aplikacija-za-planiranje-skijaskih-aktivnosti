from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),

    # authentication
    path('login/', loginRequest, name='loginRequest'),
    path('logout/', logoutRequest, name='logoutRequest'),
    path('register/', register, name='register'),
    path('instructors/', instructors, name='instructors'),
    path('map/', map, name='map'),
]