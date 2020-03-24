from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .models import Todo
from .forms import TodoForm
from django.urls import reverse
from django.utils import timezone


def home(request):
    return render(request,'todos/home.html')




def userlogin(request):
    if request.method == 'GET':
        return render(request,"todos/login.html",{'form':AuthenticationForm()})
    else:
        # TODO: Log in the user
        user_name = request.POST.get('username',False)
        pass_word = request.POST.get('password',False)
        user = authenticate(request,password=pass_word,username=user_name)

        if user is None:
            error_msg = "Failed to authenticate!"
            return render(request,"todos/login.html",{'form':AuthenticationForm(),'error_msg':error_msg})
        else:
            login(request,user)
            return redirect('todos:createtodo')



def usersignup(request):
    if request.method == 'GET':
        usr_input = request.GET.get('usr_input')
        return render(request,"todos/index.html",{'form':UserCreationForm()})
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
                return HttpResponseRedirect("todos:createtodo")
            except IntegrityError:
                error_msg = "This username is already taken!"
                return render(request,"todos/index.html",{'form':UserCreationForm(),'error_msg':error_msg})
        else:
            # TODO: password matching
            error_msg = "The passwords do not match!"
            return render(request,"todos/index.html",{'form':UserCreationForm(),'error_msg':error_msg})



def createtodo(request):

    if request.method == 'GET':
        return render(request,"todos/useraccount.html",{'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return HttpResponseRedirect(reverse("todos:curtodo"))#, args=(newtodo.id,)
        except ValueError:
            error_msg = "something went wrong!"
            return render(request,"todos/useraccount.html",{'form':TodoForm(),'error_msg':error_msg})



def curtodo(request):
    todos = Todo.objects.filter(user = request.user, completed__isnull=True)
    ctodos = Todo.objects.filter(user = request.user, completed__isnull=False)
    return render(request,"todos/curtodo.html",{'todos':todos,'ctodos':ctodos})

#def completed(request):
    #ctodos = Todo.objects.filter(user = request.user, completed__isnull=False)
    #return render(request,"todos/curtodo.html",{'ctodos':todos})


def viewtodo(request, todos_pk):
    viewTD = get_object_or_404(Todo,pk=todos_pk, user = request.user)
    if request.method == "GET":
        form = TodoForm(instance=viewTD)
        return render(request,'todos/detail.html',{'viewTD':viewTD,'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=viewTD)
            form.save()
            return HttpResponseRedirect(reverse('todos:viewtodo', args=(viewTD.id,)))#reverse('todos:viewtodo', args=(viewTD.id,)) If we want to make a reverse match by id and stay on the same page
        except ValueError:
            error_msg = "something went wrong!"
            return render(request,'todos/detail.html',{'viewTD':viewTD,'form':form,'error_msg':error_msg})

def complete(request, todos_pk):
    viewTD = get_object_or_404(Todo,pk=todos_pk, user = request.user)
    if request.method == "POST":
        viewTD.completed = timezone.now()
        viewTD.save()
        return HttpResponseRedirect(reverse('todos:curtodo'))


def deltodo(request, todos_pk):
    viewTD = get_object_or_404(Todo,pk=todos_pk, user = request.user)
    if request.method == "POST":
        viewTD.delete()
        return HttpResponseRedirect(reverse('todos:curtodo'))


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return render(request,'todos/logout.html')
