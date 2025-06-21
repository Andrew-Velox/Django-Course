from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("<h1>Welcome to the First App</h1>")
    return render(request, 'first_app/home.html')