

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [

    path('',views.index ,name="index"),
    path('signup/',views.sign_up ,name="signup"),
    path('login/',views.Log_in ,name="login"),
    path('dashboard/',views.dashboard ,name="dashboard"),
    path('logout/',views.log_out ,name="logout"),

]

