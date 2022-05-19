from django.contrib import admin
from .models import *;

# Register your models here.
admin.site.register(SkiInstructor);
admin.site.register(Activity);
admin.site.register(SkiTrack);
admin.site.register(Category);

