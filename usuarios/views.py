from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from usuarios.forms import UserLoginForm, UserRegistrationForm, UserEditForm
from usuarios.models import Usuario

def is_personal(user):
    return user.groups.filter(name="Personal").exists()

personal_required = user_passes_test(is_personal, login_url='usuario:login')

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
@personal_required
def lista_alunos(request):
    alunos = Usuario.objects.filter(groups__name='Aluno')
    return render(request, 'usuarios/lista_alunos.html', {'alunos': alunos})

@login_required
@personal_required
def aluno_updade(request, aluno_id):
    aluno = get_object_or_404(Usuario, id=aluno_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuario:aluno_perfil', args=[aluno.id]))
    else:
        form = UserEditForm(instance=aluno)
    return render(request, 'usuarios/aluno_updade.html', {'form': form, 'aluno': aluno})

@login_required
@personal_required
def aluno_perfil(request, aluno_id):
    aluno = get_object_or_404(Usuario, id=aluno_id)
    return render(request, 'usuarios/aluno_perfil.html', {'aluno': aluno})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if is_personal(user):
                        return redirect(reverse('usuario:lista_alunos'))
                    else:
                        return redirect(reverse('usuario:index'))
                else:
                    return render(request, 'usuarios/login.html', {'form': form, 'error': 'Conta desativada'})
            else:
                return render(request, 'usuarios/login.html', {'form': form, 'error': 'Login inválido'})
    else:
        form = UserLoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            try:
                group = Group.objects.get(name='Aluno')
                new_user.groups.add(group)
            except Group.DoesNotExist:
                print("O grupo 'Aluno' não existe. Certifique-se de que ele está criado no banco de dados.")
            login(request, new_user)
            return redirect(reverse('usuario:index'))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'usuarios/register.html', {'user_form': user_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('usuario:login')