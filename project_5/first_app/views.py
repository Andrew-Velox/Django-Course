from django.shortcuts import render
from . forms import makeForm,studentF
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
    if request.method == "POST":
        form = makeForm(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name,'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)

            print(form.cleaned_data)
        return render(request,'first_app/django_form.html',{"form":form})
    else:
        form=makeForm();

    return render(request,'first_app/django_form.html',{"form":form})


def students_form(request):
    if request.method == "POST":
        form = studentF(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
        
        return render(request,'first_app/django_form.html',{'form':form})
    else:
        form = studentF()
    
    return render(request,'first_app/django_form.html',{'form':form})