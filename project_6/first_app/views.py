from django.shortcuts import render,redirect
from . import models
# Create your views here.
def home(request):
    students = models.Student.objects.all()

    print(students)
    return render(request,"first_app/home.html", {'data':students})

def delete_student(request,roll):
    std = models.Student.objects.get(pk=roll).delete()
    print(std)

    return redirect("homepage")