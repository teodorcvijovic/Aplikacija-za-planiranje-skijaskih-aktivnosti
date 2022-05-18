from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
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
    errors = []

    if regform.is_valid():
        username = regform.cleaned_data.get('username')
        password1 = regform.cleaned_data.get('password1')
        password2 = regform.cleaned_data.get('password2')
        first_name = regform.cleaned_data.get('first_name')
        last_name = regform.cleaned_data.get('last_name')
        email = regform.cleaned_data.get('email')
        phone = regform.cleaned_data.get('phone')
        instagram = regform.cleaned_data.get('instagram')
        facebook = regform.cleaned_data.get('facebook')
        snapchat = regform.cleaned_data.get('snapchat')
        experience = regform.cleaned_data.get('experience')
        birthdate = regform.cleaned_data.get('birthdate')

        user = MyUser.objects.filter(username=username)

        if user:
            errors.append('Korisnik sa datim korisničkim imenom već postoji!')
        elif password1 != password2:
            errors.append('Lozinke se ne poklapaju!')
        else:
            user = SkiInstructor(username=username,
                                 password=password1,
                                 first_name=first_name,
                                 last_name=last_name,
                                 email=email,
                                 phone=phone,
                                 instagram=instagram,
                                 facebook=facebook,
                                 snapchat=snapchat,
                                 experience=experience,
                                 birthdate=birthdate)
            user.save()
            group = Group.objects.get(name="default")
            user.groups.add(group)
            login(request, user)
            return redirect('index')

    context = {
        'regform': regform,
        'errors': errors,
    }
    return render(request, 'authentication/registration.html', context)

# teodor
# page that shows all SkiInstructors
def instructors(request):
    ins = SkiInstructor.objects.all()

    # sending SkiInstructor objects without password field for safety reasons and without other unnecessary fields
    Instructors = [{
            'name': i.first_name + ' ' + i.last_name,
        } for i in ins]

    context = {
        'instructors': Instructors
    }
    return render(request, 'instructors.html', context)

# teodor
@login_required(login_url='loginRequest')
@permission_required('jahorina.delete_skiinstructor', raise_exception=True)
def deleteSkiInstructor(request):
    id = request.POST.get('skiinstructor_id')
    if id:
        ins = SkiInstructor.objects.filter(pk=id).first()
        if ins:
            ins.delete()
    return redirect('instructors')

