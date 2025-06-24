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

class studentF(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valName = self.cleaned_data['name']

    #     if len(valName) < 5:
    #         raise forms.ValidationError("Name should be more then 5 characters")
    #     else:
    #         return valName
        
    # def clean_email(self):
    #     valEmail = self.cleaned_data['email']

    #     if '@gmail' not in valEmail:
    #         raise forms.ValidationError("Email Must have @gmail")
    #     else:
    #         return valEmail


    def clean(self):
        clean_data = super().clean()
        valName = self.cleaned_data['name']
        valEmail = self.cleaned_data['email']

        if len(valName) < 5:
            raise forms.ValidationError("Name should be more then 5 characters")
        
        if '@gmail' not in valEmail:
            raise forms.ValidationError("Email Must have @gmail")



        
        