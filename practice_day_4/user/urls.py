
from django.urls import path,include
from . import views


urlpatterns = [
    path('profile/', views.profile , name="profile"),
    path('register/', views.register , name="register"),
    path('login/', views.login_frm , name="login"),
    path('logout/', views.logout_frm , name="logout"),
    path('pass_change/', views.pass_chang , name="pass_change"),
    path('pass_change2/', views.pass_chang2 , name="pass_change2"),
]
