
# teodor

import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model

'''
    Classes which represent application model. Every class represent one database table.
'''

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
    instagram = models.CharField(max_length=290, null=True, blank=True)
    facebook = models.CharField(max_length=290, null=True, blank=True)
    snapchat = models.CharField(max_length=290, null=True, blank=True)
    experience = models.IntegerField()
    birthdate = models.DateField()

    def __init__(self, *args, **kwargs):
        '''
            SkiInstructor initialization.
            :param args:
            :param kwargs:
            :return void:
        '''
        super(SkiInstructor, self).__init__(*args, **kwargs)
        # removing default username validators
        # username is validated in clean_username() method in SkiInstructorCreationForm class
        self._meta.get_field('username').validators = []


class Category(Model):
    name = models.CharField(max_length=100)
    root = models.IntegerField() # 0 - jutarnja, 1 - popodnevna, 2 - vecernja
    message = models.CharField(max_length=250, default=" ")

    def __str__(self):
        '''
            Category to String conversion.
            :return: String
        '''
        return self.name;

class Activity(Model):
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    skitrack = models.ForeignKey('SkiTrack', on_delete=models.CASCADE)  # location
    obj_name = models.CharField(max_length=100, null=True, blank=True)
    obj_contact = models.CharField(max_length=17, null=True, blank=True)

    # x and y coordinates for front-end view
    x = models.DecimalField(decimal_places=20, max_digits=21, default=0.0)
    y = models.DecimalField(decimal_places=20, max_digits=21, default=0.0)

    def __str__(self):
        '''
            Activity to String conversion.
            :return: String
        '''
        return self.obj_name + ' ' + self.obj_contact

class SkiTrack(Model):
    name = models.CharField(max_length=50)
    color = models.IntegerField() # 0 - blue, 1 - red, 2 - black
    length = models.IntegerField()
    is_foggy = models.BooleanField(default=False)
    is_opened = models.BooleanField(default=True)
    is_busy = models.BooleanField(default=False)
    last_updated = models.DateTimeField(default=datetime.datetime.now())  # SkiInstructor can update a SkiTrack
    comment=models.TextField(default='Trenutno nema novih obavestenja.', null=True, blank=True);

    def __str__(self):
        '''
            SkiTrack to String conversion.
            :return: String
        '''
        return self.name;
