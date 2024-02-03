from django import forms
from django.forms import ModelForm
from .models import PatientInfo

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PatientForm(ModelForm):
    class Meta:
        model = PatientInfo
        fields = '__all__'


class CreateProfile(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']