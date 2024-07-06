# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Treino, Execucao
from .forms import ExecucaoForm

@login_required
def treino_list(request, treino_id):
    treinos = Execucao.objects.filter(treino_id=treino_id)
    return render(request, 'treino_list.html', {'treinos': treinos, 'treino_id': treino_id})

@login_required
def treino_create(request, treino_id):
    if request.method == 'POST':
        form = ExecucaoForm(request.POST)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.treino_id = treino_id
            treino.save()
            return redirect('treino_list', treino_id=treino_id)
    else:
        form = ExecucaoForm()
    return render(request, 'treino_form.html', {'form': form, 'treino_id': treino_id})

@login_required
def treino_update(request, pk, treino_id):
    treino = get_object_or_404(Execucao, pk=pk, treino_id=treino_id)
    if request.method == 'POST':
        form = ExecucaoForm(request.POST, instance=treino)
        if form.is_valid():
            form.save()
            return redirect('treino_list', treino_id=treino_id)
    else:
        form = ExecucaoForm(instance=treino)
    return render(request, 'treino_form.html', {'form': form, 'treino_id': treino_id})

@login_required
def treino_delete(request, pk, treino_id):
    treino = get_object_or_404(Execucao, pk=pk, treino_id=treino_id)
    if request.method == 'POST':
        treino.delete()
        return redirect('treino_list', treino_id=treino_id)
    return render(request, 'treino_confirm_delete.html', {'treino': treino, 'treino_id': treino_id})
