from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegistationForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy

# Create your views here.


class UserRegistrationView(FormView):
    # template_name = 'accounts/user_registration.html'
    template_name = ''
    form_class = UserRegistationForm
    success_url = ''


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

