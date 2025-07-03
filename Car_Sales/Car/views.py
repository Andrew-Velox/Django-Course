from django.shortcuts import render,redirect
from . import forms,models
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DeleteView,DetailView

from django.contrib.auth.models import User
# Create your views here.



def car_buy(request,id):
    car = models.Car.objects.get(pk=id)
    print(car.name, car.price)
    
    car.quantity-=1
    car.save()

    models.Odred.objects.create(user=request.user, car=car)
    messages.success(request, "Purchased Successfull")
    return redirect('details',id)



class CarDetails_class(DetailView):
    model = models.Car
    template_name = 'car_dtls.html'
    
    pk_url_kwarg = 'id'


    def post(self,request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()

        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car =  self.object
        comments = car.comments.all()

        comment_form = forms.CommentForm()
        context['comments'] = comments

        context['comment_form'] = comment_form

        return context