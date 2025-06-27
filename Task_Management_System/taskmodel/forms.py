from django import forms
from . models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter task title'}),
            'task_des': forms.Textarea(attrs={'placeholder': 'Enter task description'}),
            'is_complete': forms.CheckboxInput(),
        }
