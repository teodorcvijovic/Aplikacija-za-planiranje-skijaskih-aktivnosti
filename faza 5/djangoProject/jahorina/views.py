from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import *
from .models import *

# Create your views here.

# teodor
# home page
def index(request):
    # TO DO
    context = {

    }
    return render(request, 'index.html', context)

# teodor
def loginRequest(request):
    loginform = MyLoginForm(request, request.POST or None)

    if loginform.is_valid():
        username = loginform.cleaned_data['username']
        password = loginform.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request=request, user=user)
            return redirect('index')

    context = {
        'loginform': loginform
    }
    return render(request, 'authentication/login.html', context)

# teodor
def logoutRequest(request):
    logout(request)
    return redirect('index')

# teodor
def register(request):
    regform = SkiInstructorCreationForm(request.POST)

    if regform.is_valid():
        user = regform.save()
        group = Group.objects.get(name="default")
        user.groups.add(group)
        login(request, user)

        return redirect('index')

    context = {
        'regform': regform,
    }
    return render(request, 'authentication/registration.html', context)

# teodor
# page that shows all SkiInstructors
def instructors(request):
    ins = SkiInstructor.objects.all()

    # sending SkiInstructor objects without password field for safety reasons and without other unnecessary fields
    Instructors = [{
            'name': i.first_name,
            'surname': i.last_name,
            'experience': i.experience,
            'phone': i.phone,
            'instagram': i.instagram,
            'facebook': i.facebook,
            'snapchat': i.snapchat
        } for i in ins]

    context = {
        'instructors': Instructors
    }
    return render(request, 'instructors.html', context)


def map(request):
    context = {}
    return render(request, 'map.html', context)

