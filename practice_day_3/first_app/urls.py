
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path("",include("first_app.urls")),
    path("",views.home, name="homepage"),
]
