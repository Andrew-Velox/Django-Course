from django import forms

class makeForm(forms.Form):
    name = forms.CharField(label="UserName")
    email = forms.EmailField()
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birtday = forms.DateField()
    appointment = forms.DateTimeField()