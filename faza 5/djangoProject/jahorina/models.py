import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model

class MyUser(AbstractUser):
    # fields that already exist in AbstractUser:
        # username
        # password
        # first_name
        # last_name
        # email

    phone = models.CharField(max_length=17)
    instagram = models.CharField(max_length=30, null=True)
    facebook = models.CharField(max_length=30, null=True)

    # moderator can delete SkiTracks, non-moderator Users, Services and Facilities
    is_moderator = models.BooleanField(default=False)

# every facility (restaurant, spa-center, hotel, etc.) is represented by a manager
# facility should only have one manager
class FacilityManager(MyUser):
    facility = models.ForeignKey('Facility', on_delete=models.CASCADE)

class SkiInstructor(MyUser):
    snapchat = models.CharField(max_length=30, null=True)
    skirent = models.ForeignKey('Facility', on_delete=models.DO_NOTHING, null=True) # ski-instructor can work in ski-rent facility (not required)

# static table
class FacilityType(Model):
    name = models.CharField(max_length=100)

# when user chooses to register as FacilityManager, Facility is also added to the database
class Facility(Model):
    type = models.ForeignKey(FacilityType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    skitrack = models.ForeignKey('SkiTrack', on_delete=models.CASCADE)  # facility location
    # possible change: adding x and y coordinates for frontend facility view

class SkiTrack(Model):
    name = models.CharField(max_length=50)
    color = models.IntegerField() # 0 - blue, 1 - red, 2 - black
    length = models.IntegerField()
    is_foggy = models.BooleanField(default=False)
    is_opened = models.BooleanField(default=True)
    is_busy = models.BooleanField(default=False)
    last_updated = models.DateField(default=datetime.datetime.now()) # SkiInstructor can update a SkiTrack

# FacilityManager can add services that can be included in facility's list of services
# examples:
    # restaurant - food and drinks
    # spa-center - massages
    # ski-rent - ski rent
class Service(Model):
    name = models.CharField(max_length=100)

class is_included(Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

