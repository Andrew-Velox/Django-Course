from django.shortcuts import render
from django.http import HttpResponse as http
# Create your views here.

def about(request):
    return http('second_app/about.html')

def home(request):
    return http('second_app/home.html')
