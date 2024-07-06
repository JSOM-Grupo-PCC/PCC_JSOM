# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Treino
from .forms import TreinoForm

@login_required
def programa_list(request, aluno_id):
    programas = Treino.objects.filter(aluno_id=aluno_id)
    return render(request, 'programa_list.html', {'programas': programas, 'aluno_id': aluno_id})

@login_required
def programa_create(request, aluno_id):
    personal = request.user
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.aluno_id = aluno_id
            treino.personal = personal
            treino.save()
            form.save_m2m()  # Salva relações ManyToMany após o objeto ser salvo
            return redirect('programa_list', aluno_id=aluno_id)
    else:
        form = TreinoForm()
    return render(request, 'programa_form.html', {'form': form, 'aluno_id': aluno_id})

@login_required
def programa_update(request, aluno_id, pk):
    programa = get_object_or_404(Treino, pk=pk, aluno_id=aluno_id)
    if request.method == 'POST':
        form = TreinoForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('programa_list', aluno_id=aluno_id)
    else:
        form = TreinoForm(instance=programa)
    return render(request, 'programa_form.html', {'form': form, 'aluno_id': aluno_id})

@login_required
def programa_delete(request, aluno_id, pk):
    programa = get_object_or_404(Treino, pk=pk, aluno_id=aluno_id)
    if request.method == 'POST':
        programa.delete()
        return redirect('programa_list', aluno_id=aluno_id)
    return render(request, 'programa_confirm_delete.html', {'programa': programa, 'aluno_id': aluno_id})
