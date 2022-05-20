from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.db.models import Q
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
        # first_name = regform.cleaned_data.get('first_name')
        # last_name = regform.cleaned_data.get('last_name')
        # email = regform.cleaned_data.get('email')
        # phone = regform.cleaned_data.get('phone')
        # instagram = regform.cleaned_data.get('instagram')
        # facebook = regform.cleaned_data.get('facebook')
        # snapchat = regform.cleaned_data.get('snapchat')
        # experience = regform.cleaned_data.get('experience')
        # birthdate = regform.cleaned_data.get('birthdate')

        user = MyUser.objects.filter(username=username)

        if user:
            errors.append('Korisnik sa datim korisničkim imenom već postoji!')
        elif password1 != password2:
            errors.append('Lozinke se ne poklapaju!')
        else:
            # user = SkiInstructor(username=username,
            #                      password=password1,
            #                      first_name=first_name,
            #                      last_name=last_name,
            #                      email=email,
            #                      phone=phone,
            #                      instagram=instagram,
            #                      facebook=facebook,
            #                      snapchat=snapchat,
            #                      experience=experience,
            #                      birthdate=birthdate)
            # user.save()
            user = regform.save()
            group = Group.objects.get(name="default")
            user.groups.add(group)
            login(request, user)
            return redirect('index')

    context = {
        'regform': regform,
        'errors': errors,
    }
    return render(request, 'authentication/registration.html', context)


# teodor & filip
# page that shows all SkiInstructors
def instructors(request):
    searchForm = SkiInstructorSearchForm(data=request.POST or None)
    ins = []

    if searchForm.is_valid():
        name = searchForm.cleaned_data.get('name')

        if name:
            experience = searchForm.cleaned_data.get('experience')

            if experience == 'low':
                ins = SkiInstructor.objects.filter(
                    Q(first_name__icontains=name) | Q(last_name__icontains=name), experience__lt=3
                )
            elif experience == 'mid':
                ins = SkiInstructor.objects.filter(
                    Q(first_name__icontains=name) | Q(last_name__icontains=name), experience__gte=3, experience__lt=5
                )
            elif experience == 'high':
                ins = SkiInstructor.objects.filter(
                    Q(first_name__icontains=name) | Q(last_name__icontains=name), experience__gte=5
                )
            else:
                ins = SkiInstructor.objects.filter(
                    Q(first_name__icontains=name) | Q(last_name__icontains=name)
                )
        else:
            experience = searchForm.cleaned_data.get('experience')

            if experience == 'low':
                ins = SkiInstructor.objects.filter(experience__lt=3)
            elif experience == 'mid':
                ins = SkiInstructor.objects.filter(experience__gte=3, experience__lt=5)
            elif experience == 'high':
                ins = SkiInstructor.objects.filter(experience__gte=5)
            else:
                ins = SkiInstructor.objects.filter()

    else:
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
        'searchform': searchForm,
        'instructors': Instructors
    }
    return render(request, 'instructors.html', context)

# filip
def map(request):
    context = {
        
    }
    return render(request, 'map.html', context)

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

# lara
@login_required(login_url='loginRequest')
def addActivity(request):
    categories = Category.objects.all();
    context = {
        'categories': categories
    }
    return render(request, 'addActivity.html', context);


# lara
def defineActivity(request):
    form = AddActivityForm(request.POST);
    msg = "";
    if (form.is_valid()):
        activity = form.save(commit=False);
        cat = request.POST.get("category");
        x = request.POST.get("x");
        # print(x);

        activity.type = Category.objects.get(name=cat);
        activity.save();
        msg = "Uspesno ste dodali novu aktivnost.";
        category = ""
    else:
        categoryName = request.POST.get("cat");
        category = Category.objects.get(name=categoryName);

    context = {
        'msg': msg,
        'form': form,
        'category': category,
        'request': request
    }
    return render(request, 'defineActivity.html', context);


# lara
def addCategory(request):
    form = AddCategoryForm(request.POST);
    if (form.is_valid()):
        category = form.save(commit=False);
        category.root = form.cleaned_data.get("root");
        category.save();
        return redirect('addActivity');

    else:
        context = {
            'form': form
        }
        return render(request, 'addCategory.html', context);


# lara
def planMyDayFirst(request):
    morningCategories = Category.objects.filter(root=0);
    afternoonCategories = Category.objects.filter(root=1);
    nigthCategories = Category.objects.filter(root=2);
    context = {
        'morningCategories': morningCategories,
        'afternoonCategories': afternoonCategories,
        'nightCategories': nigthCategories
    }
    return render(request, 'planMyDayFirst.html', context);


# lara
def planMyDaySecond(request):
    if (request.method == "POST"):
        checked = request.POST.getlist('checks[]');
        range = request.POST.get("range");
        # print(range);
        activities = [];
        range = int(range);
        while range >= 0:
            for c in checked:
                print(c);
                activities += Activity.objects.filter(type__name__exact=c).filter(skitrack__color__exact=range)

            range -= 1;

        context = {
            'checked': checked,
            'activities': activities
        }
        return render(request, 'planMyDaySecond.html', context);


# lara
def showTrackInformation(request):
    tracks = SkiTrack.objects.all();
    context = {
        'tracks': tracks
    }

    return render(request, 'trackInformation.html', context);


# lara
def updateTrackInformation(request):
    form = UpdateTrackForm(request.POST or None);
    trackId = request.POST.get("updateTrack");
    track = SkiTrack.objects.get(id=trackId);
    if (form.is_valid()):
        opened = form.cleaned_data.get("opened");
        # opened = request.POST.get("isOpened")
        is_foggy = form.cleaned_data.get("is_foggy");
        is_bussy = form.cleaned_data.get("is_busy")
        comment = form.cleaned_data.get("comment");
        if not comment or len(comment) == 0:
            comment = 'Nema novih obaveštenja.'
        if len(comment) > 0:
            SkiTrack.objects.filter(id=trackId).update(comment=comment);
        SkiTrack.objects.filter(id=trackId).update(is_opened=opened, is_foggy=is_foggy, is_busy=is_bussy, last_updated=datetime.datetime.now());
        return redirect('trackInformation');

    context = {
        'form': form,
        'track': track
    }

    return render(request, 'updateTrackInformation.html', context)

# teodor
@login_required(login_url='loginRequest')
def addTrack(request):
    trackform = AddTrackForm(request.POST or None)
    errors = []

    if trackform.is_valid():
        name = trackform.cleaned_data.get('name')
        #color = trackform.cleaned_data.get('color')
        color = request.POST.get('trackColor')
        length = trackform.cleaned_data.get('length')

        track = SkiTrack.objects.filter(name=name)

        if track:
            errors.append('Staza za datim nazivom već postoji')
        else:
            track = SkiTrack(name=name, color=color, length=length)
            track.save()
            return redirect('trackInformation')

    context = {
        'trackform': trackform,
        'errors': errors,
    }
    return render(request, 'addTrack.html', context)

# teodor
@login_required(login_url='loginRequest')
@permission_required('jahorina.delete_skitrack', raise_exception=True)
def deleteSkiTrack(request):
    id = request.POST.get('skitrack_id')
    if id:
        track = SkiTrack.objects.filter(pk=id).first()
        if track:
            track.delete()
    return redirect('trackInformation')

# teodor
@login_required(login_url='loginRequest')
@permission_required('jahorina.delete_category', raise_exception=True)
def deleteCategory(request):
    id = request.POST.get('category_id')
    if id:
        c = Category.objects.filter(pk=id).first()
        if c:
            c.delete()
    return redirect('addActivity')

# teodor
@login_required(login_url='loginRequest')
@permission_required('jahorina.delete_activity', raise_exception=True)
def showAllActivities(request):
    form = ActivitySearchForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data.get('name')
        if not name or len(name) == 0:
            a = Activity.objects.all()
        else:
            a = Activity.objects.filter(obj_name__icontains=name)
    else:
        a = Activity.objects.all()

    context = {
        'activities': a,
        'searchform': form,
    }
    return render(request, 'allActivities.html', context)

# teodor
@login_required(login_url='loginRequest')
@permission_required('jahorina.delete_activity', raise_exception=True)
def deleteActivity(request):
    id = request.POST.get('activity_id')
    if id:
        a = Activity.objects.filter(pk=id).first()
        if a:
            a.delete()
    return redirect('showAllActivities')


