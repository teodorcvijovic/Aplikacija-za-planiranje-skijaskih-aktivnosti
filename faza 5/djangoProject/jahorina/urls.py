from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),

    # authentication
    path('login/', loginRequest, name='loginRequest'),
    path('logout/', logoutRequest, name='logoutRequest'),
    path('register/', register, name='register'),

    # instructors
    path('instructors/', instructors, name='instructors'),
    path('deleteSkiInstructor/', deleteSkiInstructor, name='deleteSkiInstructor'),

    # day planning
    path('addActivity/', addActivity, name='addActivity'),
    path('showAllActivities/', showAllActivities, name='showAllActivities'),
    path('deleteActivity', deleteActivity, name='deleteActivity'),
    path('addCategory/', addCategory, name='addCategory'),
    path('deleteCategory/', deleteCategory, name='deleteCategory'),
    path('defineActivity/', defineActivity, name='defineActivity'),
    path('planMyDayFirst/', planMyDayFirst, name='planMyDayFirst'),
    path('planMyDaySecond/', planMyDaySecond, name='planMyDaySecond'),

    # tracks
    path('trackInformation/', showTrackInformation, name='trackInformation'),
    path('updateTrackInformation/', updateTrackInformation, name='updateTrackInformation'),
    path('deleteSkiTrack/', deleteSkiTrack, name='deleteSkiTrack'),
    path('addTrack/', addTrack, name='addTrack'),
]