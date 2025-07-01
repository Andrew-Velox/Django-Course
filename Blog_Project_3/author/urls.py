from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.user_register, name="register"),
    # path('login/', views.user_login, name="login"),
    path('login/', views.UserLoginView.as_view(), name="login"),

    path('logout/', views.user_logut, name="user_logout"),
    # path('logout/', views.UserLogoutView.as_view(), name="logout"),
    # path('logout/', views.UserLogoutView.as_view(), name='user_logout'),

    path('profile/', views.user_profile, name="profile"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('pass_change/', views.pass_change, name="pass_change"),

]
