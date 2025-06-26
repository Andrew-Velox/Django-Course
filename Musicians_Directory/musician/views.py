from django.shortcuts import render,redirect
from . import forms,models
# Create your views here.

def create_musician(request):
    if request.method =="POST":
        data = forms.MusicianForm(request.POST)

        if data.is_valid():
            data.save()
            return redirect("create_musician")
        
    else:
        data= forms.MusicianForm()
    return render(request,"create_musician.html",{'data':data})


def edit_musician(request,id):
    musician = models.Musician.objects.get(pk=id)
    data = forms.MusicianForm(instance=musician)
    if request.method =="POST":
        print(musician)
        data = forms.MusicianForm(request.POST,instance=musician)

        if data.is_valid():
            data.save()
            return redirect("homepage")
        
    
    return render(request,"create_musician.html",{'data':data})


def delete_musician(request,id):
    models.Musician.objects.get(pk=id).delete()
    return redirect("homepage")
    