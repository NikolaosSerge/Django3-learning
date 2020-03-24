from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.home,name='home'),
    path('usersignup/', views.usersignup,name='usersignup'),
    path('createtodo/', views.createtodo, name='createtodo'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('createtodo',views.createtodo, name='createtodo'),
    path('curtodo',views.curtodo, name = 'curtodo'),
    path('todos/<int:todos_pk>', views.viewtodo,name = 'viewtodo'),
    path('todos/<int:todos_pk>/complete', views.complete,name = 'complete'),
    path('todos/<int:todos_pk>/deltodo', views.deltodo,name = 'deltodo'),


]
