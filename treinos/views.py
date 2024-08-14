# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from treinos.models import Treino
from execucoes.models import Execucao
from treinos.forms import TreinoForm
from usuarios.models import Usuario

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def is_personal(user):
    return user.groups.filter(name="Personal").exists()

personal_required = user_passes_test(is_personal, login_url='usuario:login')

# +++++++++++++++++++++++++++++++++ Funcionalidades do aluno 
@login_required
@csrf_exempt
def execucao_status(request):
    if request.method == 'POST':
        execucao_id = request.POST.get('execucao_id')
        status = request.POST.get('status') == 'true'

        try:
            execucao = Execucao.objects.get(id=execucao_id)
            execucao.status = status
            execucao.save()
            return JsonResponse({'success': True})
        except Execucao.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Execucao não encontrada'})

    return JsonResponse({'success': False, 'error': 'Método inválido'})

@login_required
def meus_treinos(request):
    treinos = Treino.objects.filter(aluno=request.user).prefetch_related('execucoes__exercicio')
    return render(request, 'treinos/meus_treinos.html', {'treinos': treinos})

# +++++++++++++++++++++++++++++++++ Funcionalidades do Personal
@personal_required
def lista_treinos(request, aluno_id):
    treinos = Treino.objects.filter(aluno_id=aluno_id)
    aluno = get_object_or_404(Usuario, id=aluno_id)  # Busca os dados do aluno, ou retorna 404 se não encontrar
    return render(request, 'treinos/lista_treinos.html', 
    {
        'treinos': treinos,
        'aluno': aluno  
    })

@personal_required
def criar_treino(request, aluno_id):
    personal = get_object_or_404(Usuario, id=request.user.id)  # Converte request.user para Usuario
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.aluno_id = aluno_id
            treino.personal = personal
            treino.save()
            form.save_m2m()  # Salva relações ManyToMany após o objeto ser salvo
            return redirect('treinos:lista_treinos', aluno_id=aluno_id)
    else:
        form = TreinoForm()
    return render(request, 'treinos/treino_forms.html', {'form': form, 'aluno_id': aluno_id})

@personal_required
def editar_treino(request, aluno_id, pk):
    treino = get_object_or_404(Treino, pk=pk, aluno_id=aluno_id)
    if request.method == 'POST':
        form = TreinoForm(request.POST, instance=treino)
        if form.is_valid():
            form.save()
            return redirect('treinos:lista_treinos', aluno_id=aluno_id)
    else:
        form = TreinoForm(instance=treino)
    return render(request, 'treinos/treino_forms.html', {'form': form, 'aluno_id': aluno_id})

@personal_required
def excluir_treino(request, aluno_id, pk):
    treino = get_object_or_404(Treino, pk=pk, aluno_id=aluno_id)
    if request.method == 'POST':
        treino.delete()
    return redirect('treinos:lista_treinos', aluno_id=aluno_id)
