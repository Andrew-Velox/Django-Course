from django.urls import path,include
from . import views


urlpatterns = [
    path('register/', views.user_register, name="register"),
    path('login/', views.UserLoging_class.as_view(), name="login"),
    path('logout/', views.User_Logout, name="logout"),
    path('profile/', views.user_profile, name="profile"),
    # path('edit/', views.UserEdit_class.as_view(), name="edit"),
    path('edit/', views.edit_profile, name="edit"),
]