from django.shortcuts import render,redirect
from album.models import Album
from musician.models import Musician

def home(request):
    album = Album.objects.all()
    # print(album)
    return render(request, "home.html", {'album':album})