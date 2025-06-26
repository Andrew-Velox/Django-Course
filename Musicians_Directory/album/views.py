from django.shortcuts import render,redirect
from . import forms,models
# Create your views here.
def create_album(request):
    if request.method =="POST":
        
        data = forms.AlbumForm(request.POST)

        if data.is_valid():
            data.save()
            return redirect("create_album")
        
    else:
        data= forms.AlbumForm()
    return render(request,"create_album.html",{'data':data})

def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    data = forms.AlbumForm(instance=album)
    if request.method =="POST":
        print(album.album_name)
        data = forms.AlbumForm(request.POST,instance=album)

        if data.is_valid():
            data.save()
            return redirect("homepage")
        
    
    return render(request,"create_album.html",{'data':data})