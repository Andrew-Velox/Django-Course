
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.create_musician, name="create_musician"),
    path('edit/<int:id>', views.edit_musician, name="edit_musician"),
    path('delete/<int:id>', views.delete_musician, name="delete_musician"),
]
