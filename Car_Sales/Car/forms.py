from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name','email','body']

