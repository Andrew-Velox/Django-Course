from django import forms

class makeForm(forms.Form):
    name = forms.CharField(label="UserName",help_text="length will be less then 50 characters", required=False, widget=forms.Textarea(attrs={'id':"text_area_",'placeholder':'Your Name'}))

    # file = forms.FileField()
    # email = forms.EmailField()
    # age = forms.IntegerField()
    age = forms.CharField(widget=forms.NumberInput)
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    birtday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))

    CHOICES= [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    
    ITMS = [("P","Pepperoni"),("M","Mashroom"),("B","Beef")]
    pizza = forms.MultipleChoiceField(choices=ITMS,widget=forms.CheckboxSelectMultiple)