from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.core import validators


class SignupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']



class ChangeUserData(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']