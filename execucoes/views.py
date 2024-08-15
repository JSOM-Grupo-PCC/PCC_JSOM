from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from execucoes.models import Execucao
from treinos.models import Treino
from execucoes.forms import ExecucaoForm

def is_personal(user):
    return user.groups.filter(name="Personal").exists()

personal_required = user_passes_test(is_personal, login_url='usuario:login')

@personal_required
def lista_execucoes(request, treino_id,):
    treino = get_object_or_404(Treino, id=treino_id) 
    execucoes = Execucao.objects.filter(treino_id=treino_id)
    return render(request, 'execucoes/lista_execucoes.html', {'execucoes': execucoes, 'treino': treino})

@personal_required
def criar_execucao(request, treino_id):
    if request.method == 'POST':
        form = ExecucaoForm(request.POST)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.treino_id = treino_id
            treino.save()
            return redirect('execucoes:lista_execucoes', treino_id=treino_id)
    else:
        form = ExecucaoForm()
    return render(request, 'execucoes/execucao_form.html', {'form': form, 'treino_id': treino_id})

@personal_required
def editar_execucao(request, pk, treino_id):
    execucao = get_object_or_404(Execucao, pk=pk, treino_id=treino_id)
    if request.method == 'POST':
        form = ExecucaoForm(request.POST, instance=execucao)
        if form.is_valid():
            form.save()
            return redirect('execucoes:lista_execucoes', treino_id=treino_id)
    else:
        form = ExecucaoForm(instance=execucao)
    return render(request, 'execucoes/execucao_form.html', {'form': form, 'treino_id': treino_id})

@personal_required
def excluir_execucao(request, pk, treino_id):
    execucao = get_object_or_404(Execucao, pk=pk, treino_id=treino_id)
    if request.method == 'POST':
        execucao.delete()
    return redirect('execucoes:lista_execucoes', treino_id=treino_id)
