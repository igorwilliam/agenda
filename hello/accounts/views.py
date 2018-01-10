from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import UserForm

# Create your views here.

def addUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            return HttpResponse('Usuario Criado')
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form': form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'usuario ou senha inválido')
    return render(request, 'accounts/user_login.html')

def logoutUser(request):
    logout(request)
    return redirect('accounts:loginUser')

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha Alterada')
            return redirect('accounts:changePassword')
        else:
            messages.error(request, 'Não rolou')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
