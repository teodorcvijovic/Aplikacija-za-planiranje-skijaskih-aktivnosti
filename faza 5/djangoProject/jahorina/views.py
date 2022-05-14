from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import *
from .models import *

# Create your views here.

# teodor
# home page view
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

