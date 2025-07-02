from django.shortcuts import render,redirect
from . import forms,models

from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

# Create your views here.
# def create_album(request):
#     if request.method =="POST":
        
#         data = forms.AlbumForm(request.POST)

#         if data.is_valid():
#             data.save()
#             return redirect("create_album")
        
#     else:
#         data= forms.AlbumForm()
#     return render(request,"create_album.html",{'data':data})

@method_decorator(login_required,name='dispatch')
class create_album(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'create_album.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        
        messages.success(self.request, 'Album Created Successfully')
        return super().form_valid(form)
    

# def edit_album(request,id):
#     album = models.Album.objects.get(pk=id)
#     data = forms.AlbumForm(instance=album)
#     if request.method =="POST":
#         print(album.album_name)
#         data = forms.AlbumForm(request.POST,instance=album)

#         if data.is_valid():
#             data.save()
#             return redirect("homepage")
        
    
#     return render(request,"create_album.html",{'data':data})

@method_decorator(login_required,name='dispatch')
class edit_album_class(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'create_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')