from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required;
from django.db.models import Q;

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
            'name': i.first_name + ' ' + i.last_name,
        } for i in ins]

    context = {
        'instructors': Instructors
    }
    return render(request, 'instructors.html', context)

#lara
@login_required(login_url='loginRequest')
def addActivity(request):
    categories=Category.objects.all();
    context={
        'categories':categories
    }
    return render(request, 'addActivity.html', context);

#lara
def defineActivity(request):
    form = AddActivityForm(request.POST);
    msg="";
    if(form.is_valid()):
        activity=form.save(commit=False);
        cat=request.POST.get("category");
        x=request.POST.get("x");
        print(x);

        activity.type=Category.objects.get(name=cat);
        activity.save();
        msg="Uspesno ste dodali novu aktivnost.";
        category=""
    else:
        categoryName = request.POST.get("cat");
        category = Category.objects.get(name=categoryName);

    context = {
        'msg':msg,
        'form':form,
        'category':category,
        'request':request
    }
    return render(request, 'defineActivity.html', context);

#lara
def addCategory(request):
     form = AddCategoryForm(request.POST);
     if(form.is_valid()):
         category=form.save(commit=False);
         category.root=form.cleaned_data.get("root");
         category.save();
         return redirect('addActivity');

     else:
         context={
             'form':form
         }
         return render(request, 'addCategory.html', context);

#lara
def planMyDayFirst(request):
        morningCategories=Category.objects.filter(root=0);
        afternoonCategories=Category.objects.filter(root=1);
        nigthCategories=Category.objects.filter(root=2);
        context={
            'morningCategories':morningCategories,
            'afternoonCategories':afternoonCategories,
            'nightCategories':nigthCategories
        }
        return render(request, 'planMyDayFirst.html', context);

#lara
def planMyDaySecond(request):
    if(request.method=="POST"):
       checked = request.POST.getlist('checks[]');
       range=request.POST.get("range");
       print(range);
       activities=[];
       range = int(range);
       while range>=0:
           for c in checked:
               print(c);
               activities+=Acitivity.objects.filter(type__name__exact=c).filter(skitrack__color__exact=range)

           range-=1;

       context={
           'checked':checked,
           'activities':activities
       }
       return render(request, 'planMyDaySecond.html', context);

#lara
def showTrackInformation(request):
    tracks = SkiTrack.objects.all();
    context={
        'tracks':tracks
    }

    return render(request, 'trackInformation.html', context);

#lara
def updateTrackInformation(request):
     form = UpdateTrackForm(request.POST);
     trackId=request.POST.get("updateTrack");
     track=SkiTrack.objects.get(id=trackId);
     if(form.is_valid()):
         opened=form.cleaned_data.get("opened");
         is_foggy=form.cleaned_data.get("is_foggy");
         is_bussy=form.cleaned_data.get("is_busy")
         comment = form.cleaned_data.get("comment");
         if len(comment) > 0 :
             SkiTrack.objects.filter(id=trackId).update(comment=comment);
         SkiTrack.objects.filter(id=trackId).update(is_opened=opened, is_foggy=is_foggy, is_busy=is_bussy);
         return redirect('trackInformation');

     context={
         'form':form,
         'track':track
     }

     return render(request, 'updateTrackInformation.html', context)