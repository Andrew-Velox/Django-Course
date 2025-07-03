from django.urls import path,include
from . import views


urlpatterns = [
    path('buy/<int:id>/', views.car_buy, name="buy"),

    path('details/<int:id>/', views.CarDetails_class.as_view(), name="details"),
]