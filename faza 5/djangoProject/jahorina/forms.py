from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import Form, ModelForm, Textarea, BooleanField
from pip._internal import req

from jahorina.models import *


# teodor
class MyLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite korisničko ime'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite lozinku'})
    )

    def clean(self):
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
    username = forms.CharField(
        label='Korisničko ime',
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite korisničko ime'}),  # css class can be specified in attrs dict
        # validators=[],  # removing predefined username validators
    )
    password1 = forms.CharField(
        label='Lozinka',
        widget=forms.PasswordInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite lozinku'}),
    )
    password2 = forms.CharField(
        label='Potvrda lozinke',
        widget=forms.PasswordInput(attrs={'class': 'loginInputs', 'placeholder': 'Potvrdite unetu lozinku'}),
    )
    first_name = forms.CharField(
        label='Ime',
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite ime'})
    )
    last_name = forms.CharField(
        label='Prezime',
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite prezime'})
    )
    email = forms.EmailField(
        label='Email adresa',
        widget=forms.EmailInput(attrs={'class': 'loginInputs', 'placeholder': 'Unesite e-mail adresu'})
    )
    phone = forms.CharField(
        label='Broj telefona',
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': '+38* ** *******'})
    )
    instagram = forms.CharField(
        label='Link ka Instagram profilu',
        required=False,
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Opciono polje'})
    )
    facebook = forms.CharField(
        label='Link ka Facebook profilu',
        required=False,
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Opciono polje'})
    )
    snapchat = forms.CharField(
        label='Link ka Snapchat profilu',
        required=False,
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Opciono polje'})
    )
    experience = forms.IntegerField(
        label='Godine iskustva',
        widget=forms.NumberInput(attrs={'class': 'loginInputs', 'min': 0})
    )
    birthdate = forms.DateField(
        label='Datum rođenja',
        widget=forms.widgets.DateInput(attrs={'class': 'loginInputs', 'type': 'date'})
    )

    class Meta:
        model = SkiInstructor
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
EXP_CHOICES = [
    ('other', 'Prikaži sve'),
    ('low', 'Do 3 godine'),
    ('mid', 'Od 3 do 5 godina'),
    ('high', 'Preko 5 godina')
]

class SkiInstructorSearchForm(Form):
    name = forms.CharField(label='Ime', max_length=50, required=False)
    experience = forms.CharField(label='Iskustvo', widget=forms.Select(choices=EXP_CHOICES))

#lara
class AddActivityForm(ModelForm):
    class Meta:
        model = Activity;
        fields=['skitrack','obj_name','obj_contact'];
        labels={
            'skitrack':'Staza na kojoj se nalazi aktivnost:',
            'obj_name':'Naziv objekta:',
            'obj_contact':'Kontakt telefon objekta:',
        }

        #KOMENTAR ZA FILIPA
        #svi dijelovi forme imaju klasu "addActClass", da mozes da ih stilizujes
        def __init__(self, *args, **kwargs):
            super(AddActivityForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
            for field in self.fields.values():
                field.widget.attrs.update({'class': 'addActClass'})

#lara
class AddCategoryForm(ModelForm):
    root=forms.ChoiceField(choices=[(0,'jutarnja'), (1,'popodnevna'), (2,'vecernja')], label='Tip kategorije');
    class Meta:
        model=Category;
        fields=["name"]
        labels = {
            'name': 'Naziv kategorije:',
        }


# lara & filip
class UpdateTrackForm(ModelForm):
    CHOICES = [(1, 'Otvorena'),   (0, 'Zatvorena')]

    opened = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
        label='Stanje staze:'

    )

    class Meta:
        model = SkiTrack
        fields = ['is_foggy', 'is_busy', 'comment']
        labels = {
            'is_foggy': 'Maglovitost',
            'is_busy': 'Guzva',
            'comment': 'Komentar'
        }
        widgets = {
            'is_foggy': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_busy': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comment': forms.Textarea(attrs={'rows':3, 'cols':35, 'style': 'resize:none'}),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateTrackForm, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False


# teodor
class AddTrackForm(Form):
    name = forms.CharField(
        label='Naziv',
        widget=forms.TextInput(attrs={'placeholder': 'Unesite naziv staze'})
    )

    TRACK_COLORS = [(0, 'Plava'), (1, 'Crvena'), (2, 'Crna')]
    color = forms.ChoiceField(choices=TRACK_COLORS, widget=forms.RadioSelect, label='Boja', initial={'0', 'Plava'})

    length = forms.IntegerField(
        label='Dužina',
        widget=forms.NumberInput(attrs={'placeholder': 'Unesite dužinu u metrima', 'min': 0})
    )

