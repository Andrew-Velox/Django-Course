from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1>")
def index(request):
    return render(request, 'index.html')