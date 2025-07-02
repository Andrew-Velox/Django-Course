from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name="homepage"),
    path('',views.set_session, name="homepage"),
    # path('get/',views.get_cookie, name="get"),
    path('get/',views.get_session, name="get"),
    # path('del/',views.delete_cookie, name="del"),
    path('del/',views.delete_session, name="del"),
]
