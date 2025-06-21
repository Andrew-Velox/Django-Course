from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("This is the First App Home Page")
def courses(request):
    return HttpResponse("This is the Courses Page")

def about(request):
    return HttpResponse("This is the About Page")