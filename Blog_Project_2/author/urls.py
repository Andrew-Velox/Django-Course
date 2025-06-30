from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logut, name="logout"),
    path('profile/', views.user_profile, name="profile"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('pass_change/', views.pass_change, name="pass_change"),

]
