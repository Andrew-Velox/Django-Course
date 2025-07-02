
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registeruser, name="register"),
    path('login/', views.UserLogin.as_view(), name="login"),
    path('logout/', views.user_logout, name="logout"),
    
    # path('add/', views.create_musician, name="create_musician"),
    path('add/', views.create_musician_class.as_view(), name="create_musician"),


    # path('edit/<int:id>', views.edit_musician, name="edit_musician"),
    path('edit/<int:id>', views.edit_musician_class.as_view(), name="edit_musician"),


    # path('delete/<int:id>', views.delete_musician, name="delete_musician"),
    path('delete/<int:id>', views.delete_musician_class.as_view(), name="delete_musician"),
]
