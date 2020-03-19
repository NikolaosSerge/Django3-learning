from django.urls import path
from . import views

app_name = 'interactive_dictionary'

urlpatterns = [
    path('', views.home,name='home'),
    path('interDic/',views.interDic,name='interDic'),
]
