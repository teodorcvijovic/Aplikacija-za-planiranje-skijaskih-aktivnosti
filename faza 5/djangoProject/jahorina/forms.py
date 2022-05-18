from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import Form
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
class SkiInstructorCreationForm(Form):
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
        label='Instagram',
        required=False,
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Opciono polje'})
    )
    facebook = forms.CharField(
        label='Facebook',
        required=False,
        widget=forms.TextInput(attrs={'class': 'loginInputs', 'placeholder': 'Opciono polje'})
    )
    snapchat = forms.CharField(
        label='Snapchat',
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

    # class Meta:
    #     model = SkiInstructor
    #     fields = ['username', 'password1', 'password2', 'first_name', 'last_name',
    #               'email', 'phone', 'instagram', 'facebook', 'snapchat', 'experience', 'birthdate']

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
