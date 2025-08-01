from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login,update_session_auth_hash,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required


from posts.models import Post

# Create your views here.
# def add_author(request):
#     if request.method =="POST":
#         author_form=forms.AuthorForm(request.POST)

#         if author_form.is_valid():
#             author_form.save()
#             return redirect("add_author")
#     else:
#         author_form=forms.AuthorForm()

#     return render(request, 'add_author.html',{'form':author_form})


def user_register(request):
    if request.method =="POST":
        register_form=forms.RegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request,"Account Created Successfully")
            return redirect("profile")
    else:
        register_form=forms.RegistrationForm()

    return render(request, 'register.html',{'form':register_form, 'type':'Register'})


def user_login(request):

    if request.method =="POST":
        login_form=AuthenticationForm(request,request.POST)

        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username=user_name,password = user_pass)
            
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("profile")
            else:
                messages.warning(request,"Log in informations are incorrect")
                return redirect("register")
    else:
        login_form=AuthenticationForm()

    return render(request, 'register.html',{'form':login_form, 'type':'Login'})



@login_required
def user_profile(request):
    data = Post.objects.filter(author  = request.user)
    return render(request, 'profile.html',{'data':data})


@login_required
def edit_profile(request):
    if request.method =="POST":
        profile_form=forms.ChangeUserData(request.POST,instance=request.user)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect("profile")
    else:
        profile_form=forms.ChangeUserData(instance=request.user)

    return render(request, 'update_profile.html',{'form':profile_form, 'type':'Profile'})



def pass_change(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user, data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Password Updated Successfully")
            update_session_auth_hash(request,form.user)
            return redirect("profile")
    else:
        form=PasswordChangeForm(user=request.user)

    return render(request, 'pass_change.html',{'form':form, 'type':'Update Password'})

def user_logut(request):
    logout(request);
    return  redirect("login")