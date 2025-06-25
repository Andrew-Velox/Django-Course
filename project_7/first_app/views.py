from django.shortcuts import render
from first_app.forms import StudentForm
# Create your views here.

def home(request):
    stf = StudentForm()
    return render(request,"first_app/home.html",{"form":stf})