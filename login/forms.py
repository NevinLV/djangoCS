from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from main.models import Profile
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'loginInput', 'placeholder': 'логин', }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class' : 'loginInput', 'placeholder': 'пароль',}
))

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CreateProfileForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    #birth_date = forms.DateField(label='Дата рождения')
    profile_pic = forms.ImageField(label='Фото профиля')

    class Meta:
        model = Profile
        fields = ('name', 'surname', 'birth_date', 'profile_pic')
        widgets = {
            'birth_date': DateInput()
        }

