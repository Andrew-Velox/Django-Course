from django import forms

class makeForm(forms.Form):
    name = forms.CharField(label="UserName")

    file = forms.FileField()
    # email = forms.EmailField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birtday = forms.DateField()
    # appointment = forms.DateTimeField()

    # CHOICES= [('S','Small'),('M','Medium'),('L','Large')]
    # size = forms.ChoiceField(choices=CHOICES)
    
    # ITMS = [("P","Pepperoni"),("M","Mashroom"),("B","Beef")]
    # pizza = forms.MultipleChoiceField(choices=ITMS)