from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
# Create your views here.

def user_register(request):
    if request.method == 'POST':
        reg_form= forms.SignupForm(request.POST)

        if reg_form.is_valid():
            reg_form.save()
            messages.success(request,"Account Created Successfully")
            return redirect("homepage")
    else:
        reg_form = forms.SignupForm()

    return render(request,'register.html',{'form':reg_form,'type':"Register"})   


class UserLoging_class(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy("profile")
    
    def form_valid(self, form):
        messages.success(self.request, "Logged in Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "User Name or Password is Incorrect")
        return super().form_invalid(form)
    
    def get_contex_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Login'
        return context

def User_Logout(request):
    logout(request)
    return redirect("homepage")

@login_required
def user_profile(request):
    orders = request.user.odred_set.all()
    return render(request,'profile.html',{'type':"Profile",'user':request.user,'orders':orders})


@login_required
def edit_profile(request):
    if request.method == "POST":
        pro_form = forms.ChangeUserData(request.POST, instance=request.user)

        if pro_form.is_valid():
            pro_form.save()

            messages.success(request,"Profile Updated Successfully")
            return redirect("profile")
    
    else:
        pro_form = forms.ChangeUserData(instance=request.user)
    return render(request, "update_profile.html",{"form":pro_form,"type":"Profile"})



# @method_decorator(login_required,name='dispatch')
# class UserEdit_class(UpdateView):
#     model = User
#     form_class = forms.SignupForm
#     template_name = 'update_profile.html'
#     success_url = reverse_lazy('profile')

#     def get_object(self, queryset=None):
#         # Return the currently logged-in user
#         return self.request.user
    
#     def form_valid(self, form):
#         messages.success(self.request, "Profile Updated Successfully")
#         return super().form_valid(form)
    
#     def form_invalid(self, form):
#         messages.warning(self.request, "Wrong Informations")
#         return super().form_invalid(form)


