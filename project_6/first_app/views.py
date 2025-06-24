from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    students = models.Student.objects.all()

    print(students)
    return render(request,"first_app/home.html", {'data':students})