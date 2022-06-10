from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import Form, ModelForm, Textarea, BooleanField
from pip._internal import req

from jahorina.models import *


# teodor
class MyLoginForm(AuthenticationForm):
    '''
        MyLoginForm: Form used for user authentication.
    '''

    '''
        username: forms.CharField
    '''
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite korisničko ime'})
    )
    '''
        password: forms.CharField
    '''
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite lozinku'})
    )

    def clean(self):
        '''
            Method called after data is collected from all form fields.
            :return: Dictionary:
        '''
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = MyUser.objects.filter(username=username).first()

        if not user:
            raise forms.ValidationError('Korisnik nije registrovan!')
        elif not authenticate(username=username, password=password):
            raise forms.ValidationError('Uneli ste neispravnu lozinku!')

        return self.cleaned_data


# teodor
class SkiInstructorCreationForm(UserCreationForm):
    '''
        SkiInstructorCreationForm: Form used for user registration.
    '''

    '''
        username: forms.CharField
    '''
    username = forms.CharField(
        label='Korisničko ime',
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite korisničko ime'}),  # css class can be specified in attrs dict
        # validators=[],  # removing predefined username validators
    )
    '''
        password1: forms.CharField
    '''
    password1 = forms.CharField(
        label='Lozinka',
        widget=forms.PasswordInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite lozinku'}),
    )
    '''
        password2: forms.CharField
    '''
    password2 = forms.CharField(
        label='Potvrda lozinke',
        widget=forms.PasswordInput(attrs={'class': 'loginInputs', 'placeholder': 'Potvrdite unetu lozinku'}),
    )
    '''
        first_name: forms.CharField
    '''
    first_name = forms.CharField(
        label='Ime',
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite ime'})
    )
    '''
        last_name: forms.CharField
    '''
    last_name = forms.CharField(
        label='Prezime',
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite prezime'})
    )
    '''
        email: forms.EmailField
    '''
    email = forms.EmailField(
        label='Email adresa',
        widget=forms.EmailInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite e-mail adresu'})
    )
    '''
        phone: forms.CharField
    '''
    phone = forms.CharField(
        label='Broj telefona',
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': '+38* ** *******'})
    )
    '''
        instagram: forms.CharField
    '''
    instagram = forms.CharField(
        label='Link ka Instagram profilu',
        required=False,
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Opciono polje'})
    )
    '''
        facebook: forms.CharField
    '''
    facebook = forms.CharField(
        label='Link ka Facebook profilu',
        required=False,
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Opciono polje'})
    )
    '''
        snapchat: forms.CharField
    '''
    snapchat = forms.CharField(
        label='Link ka Snapchat profilu',
        required=False,
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Opciono polje'})
    )
    '''
        experience: forms.IntegerField
    '''
    experience = forms.IntegerField(
        label='Godine iskustva',
        widget=forms.NumberInput(attrs={'class': 'loginInputs', 'min': 0})
    )
    '''
        birthdate: forms.DateField
    '''
    birthdate = forms.DateField(
        label='Datum rođenja',
        widget=forms.widgets.DateInput(attrs={'class': 'loginInputs', 'type': 'date'})
    )

    class Meta:
        '''
            model: SkiInstructor
        '''
        model = SkiInstructor
        '''
            fields: Array of String
        '''
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name',
                  'email', 'phone', 'instagram', 'facebook', 'snapchat', 'experience', 'birthdate']

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #
    #     user = MyUser.objects.filter(username=username).first()
    #
    #     if user:
    #         raise forms.ValidationError('Korisnik sa datim korisničkim imenom već postoji!')
    #

# filip
class SkiInstructorSearchForm(Form):
    '''
        SkiInstructorSearchForm: Form used for SkiInstructor search by multiple criteria.
    '''

    '''
        EXP_CHOICES: Array of Tuple
    '''
    EXP_CHOICES = [
        ('other', 'Prikaži sve'),
        ('low', 'Do 3 godine'),
        ('mid', 'Od 3 do 5 godina'),
        ('high', 'Preko 5 godina')
    ]

    '''
        name: forms.CharField    
    '''
    name = forms.CharField(label='Ime', max_length=50, required=False)
    '''
        experience: forms.CharField    
    '''
    experience = forms.CharField(label='Iskustvo', widget=forms.Select(choices=EXP_CHOICES))

# filip
class ActivitySearchForm(Form):
    '''
        ActivitySearchForm: Form used for activity search. Used only by moderators/administrator.
    '''

    '''
        name: forms.CharField
    '''
    name = forms.CharField(label='Ime', max_length=50, required=False)


#lara & filip
class AddActivityForm(ModelForm):
    '''
        AddActivityForm: Form used for adding new Activity.
    '''

    class Meta:
        '''
            model: Activity
        '''
        model = Activity;
        '''
            fields: Array of String
        '''
        fields=['skitrack','obj_name','obj_contact'];
        '''
            labels: Dictionary
        '''
        labels={
            'skitrack':'Staza na kojoj se nalazi aktivnost:',
            'obj_name':'Naziv objekta:',
            'obj_contact':'Kontakt telefon objekta:',
        }
        '''
            widgets: Dictionary
        '''
        widgets = {
            'skitrack': forms.Select(attrs={'class': 'form-select'}),
            'obj_name': forms.TextInput(attrs={'required': 'true'}),
            'obj_contact': forms.TextInput(attrs={'required': 'true'})
        }

        def __init__(self, *args, **kwargs):
            '''
                AddActivityForm's Meta class initialization.
                :param args:
                :param kwargs:
                :return void:
            '''
            super(AddActivityForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
            for field in self.fields.values():
                field.widget.attrs.update({'class': 'addActClass'})


#lara
class AddCategoryForm(ModelForm):
    '''
        AddCategoryForm: Form used for adding new Category.
    '''

    # root=forms.ChoiceField(choices=[(0,'jutarnja'), (1,'popodnevna'), (2,'vecernja')], label='Tip kategorije');

    '''
        message: forms.CharField
    '''
    message=forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 30, 'placeholder' : 'Unesite Vašu poruku'}), required=False)

    class Meta:
        '''
            model: Category
        '''
        model=Category;
        '''
            fields: Array of String
        '''
        fields=["name"]
        '''
            labels: Dictionary
        '''
        labels = {
            'name': 'Naziv kategorije:',
        }


# lara & filip
class UpdateTrackForm(ModelForm):
    '''
        UpdateTrackForm: Form used for updating SkiTrack information. Only used by authenticated users.
    '''

    '''
        CHOICES: Array of Tuple
    '''
    CHOICES = [(1, 'Otvorena'),   (0, 'Zatvorena')]

    '''
        opened: forms.ChoiceField
    '''
    opened = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
        label='Stanje staze:'
    )

    class Meta:
        '''
            model: SkiTrack
        '''
        model = SkiTrack
        '''
            fields: Array of String
        '''
        fields = ['is_foggy', 'is_busy', 'comment']
        '''
            labels: Dictionary
        '''
        labels = {
            'is_foggy': 'Maglovitost',
            'is_busy': 'Guzva',
            'comment': 'Komentar'
        }
        '''
            widget: Dictionary
        '''
        widgets = {
            'is_foggy': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_busy': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comment': forms.Textarea(attrs={'rows':3, 'cols':35, 'style': 'resize:none', 'placeholder': 'Opciono polje'}),
        }

    def __init__(self, *args, **kwargs):
        '''
            UpdateTrackForm object initialization.
            :param args:
            :param kwargs:
            :return void:
        '''
        super(UpdateTrackForm, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False


# teodor
class AddTrackForm(Form):
    '''
        AddTrackForm: Form used for adding new SkiTrack.
    '''

    '''
        name: forms.CharField
    '''
    name = forms.CharField(
        label='Naziv',
        widget=forms.TextInput(attrs={'placeholder': 'Unesite naziv staze'})
    )

    # TRACK_COLORS = [(0, 'Plava'), (1, 'Crvena'), (2, 'Crna')]
    # color = forms.ChoiceField(
    #     choices=TRACK_COLORS,
    #     widget=forms.RadioSelect,
    #     label='Boja',
    #     initial={'0', 'Plava'},
    #     required=False
    # )

    '''
        length: forms.IntegerField
    '''
    length = forms.IntegerField(
        label='Dužina',
        widget=forms.NumberInput(attrs={'placeholder': 'Dužina u metrima', 'min': 0})
    )

