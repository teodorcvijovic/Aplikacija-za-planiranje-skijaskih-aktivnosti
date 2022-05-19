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
    path('addActivity/', addActivity, name='addActivity'),
    path('addCategory/', addCategory, name='addCategory'),
    path('defineActivity/', defineActivity, name='defineActivity'),
    path('planMyDayFirst/', planMyDayFirst, name='planMyDayFirst'),
    path('planMyDaySecond/', planMyDaySecond, name='planMyDaySecond'),
    path('trackInformation/', showTrackInformation, name='trackInformation'),
    path('updateTrackInformation/', updateTrackInformation, name='updateTrackInformation')
]