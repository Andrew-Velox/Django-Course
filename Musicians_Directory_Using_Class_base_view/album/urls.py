from django.urls import path
from . import views

urlpatterns = [
    # path('add/', views.create_album, name="create_album"),
    path('add/', views.create_album.as_view(), name="create_album"),


    # path('edit/<int:id>', views.edit_album, name="edit_album"),
    path('edit/<int:id>', views.edit_album_class.as_view(), name="edit_album"),
]
