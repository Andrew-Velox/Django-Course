from django.shortcuts import render,redirect
from . import forms

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.


@login_required
def profile(request):
    return render(request,"home.html",{'type':"Profile"})

def register(request):
    if request.method == "POST":
        reg_form = forms.RegisterForm(request.POST)

        if reg_form.is_valid():
            reg_form.save()
            messages.success(request,"Account Created Successfully")
            return redirect("profile")
    else:
        reg_form=forms.RegisterForm()
    
    return render(request,"register.html",{'form':reg_form,'type':'Register'})

def login_frm(request):
    if request.method=="POST":
        log_form =  AuthenticationForm(request,request.POST)

        if log_form.is_valid():
            user_name = log_form.cleaned_data['username']  
            user_pass = log_form.cleaned_data['password']


            user = authenticate(username=user_name,password=user_pass)

            if user is not None:
                login(request,user)
                messages.success(request,"Logged In Successfully")
                print(messages)
                return redirect("profile")
            else:
                messages.warning(request,"Log in information is Incorrect")
                return redirect("login")
    else:
        log_form=AuthenticationForm()
    
    return render(request,"register.html",{'form':log_form, 'type':"Login"})




def logout_frm(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect("homapage")
    


def pass_chang(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(request.user, data=request.POST)

            if form.is_valid():
                form.save()
                messages.success(request,"Password Change Successfully")
                update_session_auth_hash(request,form.user)
                return redirect("profile")
        
        else:
            form = PasswordChangeForm(user=request.user)
        
        return render(request,"pass_chng.html",{'form':form,'type':"Change Password"})
    else:
        return redirect("homapage")

def pass_chang2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(request.user, data=request.POST)

            if form.is_valid():
                form.save()
                messages.success(request,"Password Change Successfully")
                update_session_auth_hash(request,form.user)
                return redirect("profile")
        
        else:
            form = SetPasswordForm(user=request.user)
        
        return render(request,"pass_chng.html",{'form':form,'type':"Change Password"})
    else:
        return redirect("homapage")



