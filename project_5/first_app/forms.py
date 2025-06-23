from django import forms

class makeForm(forms.Form):
    name = forms.CharField(label="UserName")
    email = forms.EmailField()