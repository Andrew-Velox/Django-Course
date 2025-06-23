from django.shortcuts import render
from . forms import makeForm
# Create your views here.
def home(request):
    return render(request, "first_app/home.html")


def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')

        return render(request,'first_app/about.html',{"name":name, "email":email,"select":select})
    

    return render(request,"first_app/about.html")


def form(request):
    
    return render(request,"first_app/form.html")

def django_form(request):
    form = makeForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'first_app/django_form.html',{"form":form})