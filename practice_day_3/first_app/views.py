from django.shortcuts import render
from . forms import MakeForm
# Create your views here.


def home(request):
    if request.method=="POST":
        form = MakeForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            return render(request,'home.html',{"form":form})
    else:
        form= MakeForm()
    return render(request,'home.html',{"form":form})