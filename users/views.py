"""Vista de usuarios"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

#forms
from users.forms import ProfileForm, SignupForm

@login_required
def update_profile(request):
    """Actualizacion de perfil"""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            data = form.cleaned_data
            
            profile.webiste=data['website']
            profile.phone_number=data['phone_number']
            profile.biography=data['biography']
            profile.picture=data['picture']
            profile.save()
            
            return redirect('update_profile')
    else:
        form = ProfileForm()
    
    return render(
        request =request,
        template_name='users/update_profile.html',
        context = {
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


def login_view(request):
    """Vista de login"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html',{'error':'Usuario o contraseña incorrecto'})
    return render(request, 'users/login.html') 


def signup(request):
    """Vista de registro de usuario"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    
    return render(
        request =request,
        template_name='users/signup.html',
        context = {
            'form': form
        }
    )    

@login_required
def logout_view(request):
    """Vista de cerrar sesion"""
    logout(request)
    return redirect('login')