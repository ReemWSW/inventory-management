from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserForm

# Create your views here.

def register_view(request):
    if request.method == "POST":

        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('auth:login')

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request, 
                          template_name = "auth/register.html", 
                          context={"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('auth:profile')
        
        else:
            form = AuthenticationForm()
        return render(request, 'auth/login.html', {'form': form})