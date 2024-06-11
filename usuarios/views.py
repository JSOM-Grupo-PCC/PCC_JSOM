from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@login_required
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('usuario:index'))  # Alterado para redirecionar para 'index'
                else:
                    return render(request, 'usuarios/login.html', {'form': form, 'error': 'Conta desativada'})
            else:
                return render(request, 'usuarios/login.html', {'form': form, 'error': 'Login inválido'})
    else:
        form = UserLoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('usuario:login')  # Redireciona para a página de login após o logout

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            # Adiciona o novo usuário ao grupo de alunos
            group = Group.objects.get(name='Aluno')
            new_user.groups.add(group)
            login(request, new_user)  # Faz o login do usuário automaticamente
            return redirect(reverse('usuario:index'))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'usuarios/register.html', {'user_form': user_form})