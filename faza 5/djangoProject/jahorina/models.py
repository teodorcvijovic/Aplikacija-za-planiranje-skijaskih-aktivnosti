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

    # moderator can delete SkiTracks, non-moderator Users, Acitivites and Categories
    is_moderator = models.BooleanField(default=False)


class SkiInstructor(MyUser):
    phone = models.CharField(max_length=17)
    instagram = models.CharField(max_length=30, null=True, blank=True)
    facebook = models.CharField(max_length=30, null=True, blank=True)
    snapchat = models.CharField(max_length=30, null=True, blank=True)
    experience = models.IntegerField()
    birthdate = models.DateField()

    def __init__(self, *args, **kwargs):
        super(SkiInstructor, self).__init__(*args, **kwargs)
        # removing default username validators
        # username is validated in clean_username() method in SkiInstructorCreationForm class
        self._meta.get_field('username').validators = []

class Category(Model):
    name = models.CharField(max_length=100)
    root = models.IntegerField() # 0 - jutarnja, 1 - popodnevna, 2 - vecernja


class Acitivity(Model):
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    skitrack = models.ForeignKey('SkiTrack', on_delete=models.CASCADE)  # location
    obj_name = models.CharField(max_length=100, null=True, blank=True)
    obj_contact = models.CharField(max_length=17, null=True, blank=True)
    # possible change: adding x and y coordinates for front-end view


class SkiTrack(Model):
    name = models.CharField(max_length=50)
    color = models.IntegerField() # 0 - blue, 1 - red, 2 - black
    length = models.IntegerField()
    is_foggy = models.BooleanField(default=False)
    is_opened = models.BooleanField(default=True)
    is_busy = models.BooleanField(default=False)
    last_updated = models.DateField(default=datetime.datetime.now()) # SkiInstructor can update a SkiTrack

