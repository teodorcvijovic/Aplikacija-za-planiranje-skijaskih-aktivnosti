from django.contrib import admin

# Register your models here.
from jahorina.models import *
from django.contrib.auth.models import Group

admin.site.register(SkiTrack)
admin.site.register(SkiInstructor)
admin.site.register(Activity)
admin.site.register(Category)
