from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserForm, UserUpdateForm

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
                          context={"form":form})

    form = UserForm
    return render(request = request,
                  template_name = "auth/register.html",
                  context={"form":form})

#! login
def login_view(request):
    if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('auth:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {
        'form': form
    })

#! logout    
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("auth:register")


#! profile
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('auth:profile')

    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'form': form
    }

    return render(request, 'auth/profile.html', context)

def delete_view(request, pk):
    form = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('auth:login')
    return render(request, 'auth/delete.html', {'form': form})