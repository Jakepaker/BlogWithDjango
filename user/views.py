from django.shortcuts import render, redirect
from .forms import Registration, Login
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password

# Create your views here.
def RegisterView(request):
    form = Registration(request.POST) if request.method == "POST" else Registration()
    if form.is_valid():
        cleaned_form = form.clean()
        cleaned_form['password'] = make_password(cleaned_form['password'])
        User.objects.create(**cleaned_form)
        return render(request, 'home.html')
    return render(request, 'register.html', {'form': form})

def LoginView(request):
    form = Login(request.POST) if request.method == 'POST' else Login()
    if form.is_valid():
        get_credential = form.clean()
        user = auth.authenticate(**get_credential)
        if user is not None:
            auth.login(request,user)
            return render(request,'userhomepage.html')
        messages.error(request, 'wrong credential')
    return render(request, 'login.html', {'form': form})

def LogoutView(request):
    auth.logout(request)
    return redirect('blog.home')