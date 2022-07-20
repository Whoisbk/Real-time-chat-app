from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm  
from .forms import SigninUser
# Create your views here.
 #request.POST.get('new_subject')
def signin(request):
    if request.method == "POST":
        form = SigninUser(request.POST)
        if form.is_valid():
            user = form.cleaned_data["username"]
            pass1 = form.cleaned_data["pass1"]
            
            u = authenticate(username=user,password=pass1)

            if u is not None:
                login(request,u)
                return redirect('main')
            else:
                messages.error(request,'Incorrect credentials')
                return redirect('signin')
    else:
        form = SigninUser(request.POST)
    
    context = {'form':form}

    return render(request,'Chat/login.html',context)

def register(request):
    
    if request.method == "POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            print('hello') 
            messages.success(request,"User Created")
            return redirect('signin')
    else:
        form = UserCreationForm()
        print('hello')
    context = {"form":form}
    
    return render(request,'Chat/register.html',context)


def main(request):
    
    return render(request,'Chat/main.html')

def lobby(request,lobby_name):
    context = {'lobby_name':lobby_name}
    return render(request,'Chat/lobby.html',context)
