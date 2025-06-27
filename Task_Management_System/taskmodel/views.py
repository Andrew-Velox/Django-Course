from django.shortcuts import render,redirect
from . import forms,models
from taskmodel.models import Task
from taskcategory.models import Category
# Create your views here.


def add_task(request):
    if request.method == "POST":
        task_form = forms.TaskForm(request.POST)

        if task_form.is_valid():
            task_form.save()
            return redirect("show_task")
    else:
        task_form=forms.TaskForm()
    return render(request, "add_task.html",{"form":task_form})


def show_task(request):
    task = Task.objects.all()
    # print(all)
    return render(request,"show_task.html",{"task":task})

def edit_task(request,id):
    task= models.Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    # print(task_form)

    if request.method == "POST":
        task_form = forms.TaskForm(request.POST,instance=task)

        if task_form.is_valid():
            task_form.save()
            return redirect("show_task")
    return render(request,"add_task.html",{"form":task_form})

def delete_task(request,id):
    models.Task.objects.get(pk=id).delete()
    return redirect("show_task")