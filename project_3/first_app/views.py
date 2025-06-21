from django.shortcuts import render

# Create your views here.

def home(request):
    dictionary = {
        'Name': 'Andrew',
        'Age' : 20,
        'Hobbies': ['Reading', 'Gaming', 'Coding'],

    }
    return render(request, 'first_app/home.html', context=dictionary)

