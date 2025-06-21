from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    dictionary = {
        'Name': 'Andrew',
        'Age' : 4,
        'Hobbies': ['Reading', 'Gaming', 'Coding'],
        'Current_Date': datetime.datetime.now(),
        'Courses':[
            {
                'Name': 'Python',
                'Duration': '3 months',
                'Rating': 4.5
            },
            {
                'Name': 'Django',
                'Duration': '2 months',
                'Rating': 4.8
            },
            {
                'Name': 'JavaScript',
                'Duration': '1 month',
                'Rating': 4.2
            }

        ]

    }
    return render(request, 'first_app/home.html', dictionary)

