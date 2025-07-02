from django.shortcuts import render,redirect
from . import forms,models
from django.contrib import messages
from django.contrib.auth import login,logout


from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

def registeruser(request):
    if request.method == "POST":
        reg_form = forms.RegisterForm(request.POST)
    
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request,"Account Created Successfully")
            return redirect("login")
    else:
        reg_form = forms.RegisterForm()

    return render(request, 'register.html',{'form':reg_form,'type':"Register"})

class UserLogin(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy("homepage")
    
    def form_valid(self, form):
        messages.success(self.request, "Logged In Succefully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, "Username or Password is Invalid")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
def user_logout(request):
    logout(request)
    return redirect("login")








# def create_musician(request):
#     if request.method =="POST":
#         data = forms.MusicianForm(request.POST)

#         if data.is_valid():
#             data.save()
            
#             return redirect("create_musician")
    
        
#     else:
#         data= forms.MusicianForm()
#     return render(request,"create_musician.html",{'form':data})

@method_decorator(login_required,name='dispatch')
class create_musician_class(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'create_musician.html'
    success_url = reverse_lazy('create_musician')

    def form_valid(self, form):
        messages.success(self.request, 'Musician Created Successfully')
        return super().form_valid(form)
    


# def edit_musician(request,id):
#     musician = models.Musician.objects.get(pk=id)
#     data = forms.MusicianForm(instance=musician)
#     if request.method =="POST":
#         print(musician)
#         data = forms.MusicianForm(request.POST,instance=musician)

#         if data.is_valid():
#             data.save()
#             return redirect("homepage")
        
    
#     return render(request,"create_musician.html",{'form':data})

@method_decorator(login_required,name='dispatch')
class edit_musician_class(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm

    template_name = 'create_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


# def delete_musician(request,id):
#     models.Musician.objects.get(pk=id).delete()
#     return redirect("homepage")

@method_decorator(login_required,name='dispatch')
class delete_musician_class(DeleteView):
    model= models.Musician
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')