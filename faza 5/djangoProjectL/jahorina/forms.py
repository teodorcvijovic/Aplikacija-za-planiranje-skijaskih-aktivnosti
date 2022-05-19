from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import ModelForm;
from .models import Acitivity;

from jahorina.models import *

# teodor
class MyLoginForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = MyUser.objects.filter(username=username).first()

        if not user:
            raise forms.ValidationError('Korisnik nije registrovan!')
        elif user.password != password:
            raise forms.ValidationError('Uneli ste neispravnu lozinku!')

        return self.cleaned_data

# teodor
class SkiInstructorCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Korisničko ime',
        widget=forms.TextInput(),  # css class can be specified in attrs dict
        validators=[]  # removing predefined username validators
    )
    password1 = forms.CharField(
        label='Lozinka',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Potvrda lozinke',
        widget=forms.PasswordInput()
    )
    first_name = forms.CharField(
        label='Ime',
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        label='Prezime',
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        label='Email adresa',
        widget=forms.EmailInput()
    )
    phone = forms.CharField(
        label='Broj telefona',
        widget=forms.TextInput(attrs={'placeholder': '+38* ** *******'})
    )
    instagram = forms.CharField(
        label='Instagram',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Opciono polje'})
    )
    facebook = forms.CharField(
        label='Facebook',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Opciono polje'})
    )
    snapchat = forms.CharField(
        label='Snapchat',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Opciono polje'})
    )
    experience = forms.IntegerField(
        label='Godine iskustva',
        widget=forms.NumberInput(attrs={'min': 0})
    )
    birthdate = forms.DateField(
        label='Datum rođenja',
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = SkiInstructor
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name',
                  'email', 'phone', 'instagram', 'facebook', 'snapchat', 'experience', 'birthdate']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        user = MyUser.objects.filter(username=username).first()

        if user:
            raise forms.ValidationError('Korisnik sa datim korisničkim imenom već postoji!')

        return self.cleaned_data

    def clean_password2(self):
        # TO DO: front-end
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Lozinke se ne poklapaju!')

        return self.cleaned_data

    # def clean_phone(self):
    #     pass
    #     # TO DO: front-end
    #
    # def clean_birthdate(self):
    #     pass
    #     # TO DO: front-end


#lara
class AddActivityForm(ModelForm):
    class Meta:
        model = Acitivity;
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

#lara
class UpdateTrackForm(ModelForm):
    CHOICES = [(1, 'Otvorena'),   (0, 'Zatvorena')]

    opened = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='Stanje staze:')
    class Meta:
        model=SkiTrack;
        fields=['is_foggy','is_busy','comment'];
        labels={
            'is_foggy' : 'Maglovitost:',
            'is_busy':'Guzva:',
            'comment':'Komentar'
        }

