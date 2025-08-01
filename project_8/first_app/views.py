from django.shortcuts import render,redirect
from . forms import RegisterForm,UserEditForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            print(form.cleaned_data)
            
    else:
        form=RegisterForm()
    return render(request, "signup.html",{'form':form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            passw = form.cleaned_data['password']


            user = authenticate(username=name, password=passw) #user database a ache kina

            if user is not None:
                login(request,user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})



def profile(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    if request.method=="POST":
        form = UserEditForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Update successful.')
            
    else:
        form=UserEditForm(instance=request.user)
    return render(request, "profile.html",{'form':form})


def user_logout(request):
    logout(request)
    return redirect("login")


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user= request.user, data= request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)

                return redirect("profile")
            
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "passchange.html", {'form': form})
    else:
        return redirect("login")
    

    
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user= request.user, data= request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)

                return redirect("profile")
            
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, "passchange.html", {'form': form})
    else:
        return redirect("login")