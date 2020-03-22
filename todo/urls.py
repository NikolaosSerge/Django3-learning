from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home,name='home'),
    path('usersignup/', views.usersignup,name='usersignup'),
    path('useraccount/', views.useraccount, name='useraccount'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('userlogin/', views.userlogin, name='userlogin'),


]
