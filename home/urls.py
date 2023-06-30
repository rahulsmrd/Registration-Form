from django.contrib import admin
from django.urls import path,include
from home import views


app_name='home'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path("logout/",views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path("dashboard/",views.dashboard,name='dashboard'),
]
