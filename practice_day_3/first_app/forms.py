from django import forms
from django.core import validators
import datetime

class MakeForm(forms.Form):
    name=forms.CharField(help_text="Length will be less then 50 characters")
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':"yy-mm-dd"}))
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982','2004']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_address = forms.EmailField(required = False)
    message = forms.CharField(max_length = 10,required=False)
    email_addresss = forms.EmailField(label="Please enter your email address",required=False)
    first_name = forms.CharField(initial="Your name")
    agrees = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)


    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]

    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_colors = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    favorite_colorsss = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_colorssss = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

    