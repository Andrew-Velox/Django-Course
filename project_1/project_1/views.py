from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the Home Page")

def contact(request):
    return HttpResponse("Contact us at")