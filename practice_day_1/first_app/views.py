from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    dictionary = {
        "text" : ["Thiss","is","string", "array"],
        "people" : [
            {'name': 'Josh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
        ],
        "datetime":datetime.datetime.now(),
    }
    return render(request,"first_app/home.html", dictionary)

def about(request):
    return render(request,"first_app/about.html")

def contact(reqeust):
    return render(reqeust,"first_app/contact.html")