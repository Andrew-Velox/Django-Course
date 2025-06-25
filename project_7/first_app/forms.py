from django import forms

from first_app.models import StudentModel

class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name','roll']
        labels = {
            'name': "Student Name",
            'roll': "Student Roll"
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':' btn btn-primary'}),
            'roll': forms.PasswordInput()
        }

        help_texts ={
            'name': "Enter Your Full Name",
        }
        error_messages={
            'name': {"required":"Please Enter Your Name"}
        }