from django.shortcuts import render
from . forms import MakeForm
from . models import MakeModelForm
# from . import models
# Create your views here.


def home(request):
    #---------this is for the form fileds
    # if request.method=="POST":
    #     form = MakeForm(request.POST)

    #     if form.is_valid():
    #         # print(form.cleaned_data)
    #         return render(request,'home.html',{"form":form})
    # else:
    #     form= MakeForm()

    # ---------------this is for the Model Form-------
    data = MakeModelForm.objects.all()
    print(data)
    return render(request,'home.html',{"form":data})