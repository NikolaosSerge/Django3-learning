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
from django.contrib.auth.decorators import login_required

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
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('todos:home')
        return render(request, 'todos/index.html', {'form': form})
    return render(request, 'todos/index.html')





@login_required
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


@login_required
def curtodo(request):
    todos = Todo.objects.filter(user = request.user, completed__isnull=True).order_by('-created')
    ctodos = Todo.objects.filter(user = request.user, completed__isnull=False).order_by('-completed')
    return render(request,"todos/curtodo.html",{'todos':todos,'ctodos':ctodos})

#def completed(request):
    #ctodos = Todo.objects.filter(user = request.user, completed__isnull=False)
    #return render(request,"todos/curtodo.html",{'ctodos':todos})

@login_required
def viewtodo(request, todos_pk):
    viewTD = get_object_or_404(Todo,pk=todos_pk, user = request.user)
    #if  viewTD.completion is True:
        #return render(request,'todos/comdetail.html')
    if request.method == "GET":
        form = TodoForm(instance=viewTD)
        return render(request,'todos/detail.html',{'viewTD':viewTD,'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=viewTD)
            form.save()
            return HttpResponseRedirect(reverse('todos:curtodo'))#reverse('todos:viewtodo', args=(viewTD.id,)) If we want to make a reverse match by id and stay on the same page
        except ValueError:
            error_msg = "something went wrong!"
            return render(request,'todos/detail.html',{'viewTD':viewTD,'form':form,'error_msg':error_msg})

@login_required
def complete(request, todos_pk):
    viewTD = get_object_or_404(Todo,pk=todos_pk, user = request.user)
    if request.method == "POST":
        viewTD.completed = timezone.now()
        viewTD.completion = True
        viewTD.save()
        return HttpResponseRedirect(reverse('todos:curtodo'))

@login_required
def deltodo(request, todos_pk):
    viewTD = get_object_or_404(Todo,pk=todos_pk, user = request.user)
    if request.method == "POST":
        viewTD.delete()
        return HttpResponseRedirect(reverse('todos:curtodo'))

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return render(request,'todos/logout.html')



def play(request):
    return render(request,'todos/play.html')
