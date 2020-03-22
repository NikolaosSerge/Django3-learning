from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate

def home(request):
    return render(request,'todo/home.html')

def userlogin(request):
    if request.method == 'GET':
        return render(request,"todo/login.html",{'form':AuthenticationForm()})
    else:
        # TODO: Log in the user
        user_name = request.POST.get('username',False)
        pass_word = request.POST.get('password',False)
        user = authenticate(request,password=pass_word,username=user_name)

        if user is None:
            error_msg = "Failed to authenticate!"
            return render(request,"todo/index.html",{'form':AuthenticationForm(),'error_msg':error_msg})
        else:
            login(request,user)
            return redirect('todo:useraccount')







def usersignup(request):
    if request.method == 'GET':
        usr_input = request.GET.get('usr_input')
        return render(request,"todo/index.html",{'form':UserCreationForm()})
    else:
        # TODO: Create a new user
        usr_name = request.POST.get('username',False)
        password1 = request.POST.get('password1',False)
        password2 = request.POST.get('password2',False)
        if password1 == password2:
            try:
                user = User.objects.create_user(usr_name,password = password1)
                user.save()
                login(request,user)
                return redirect("todo:useraccount")
            except IntegrityError:
                error_msg = "This username is already taken!"
                return render(request,"todo/index.html",{'form':UserCreationForm(),'error_msg':error_msg})

        else:
            # TODO: password matching
            error_msg = "The passwords do not match!"
            return render(request,"todo/index.html",{'form':UserCreationForm(),'error_msg':error_msg})

def useraccount(request):
    return render(request,"todo/useraccount.html")

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return render(request,'todo/logout.html')
