from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from avaliacoes.models import Avaliacao
from avaliacoes.forms import AvaliacaoForm
from usuarios.models import Usuario

def is_personal(user):
    return user.groups.filter(name="Personal").exists()

personal_required = user_passes_test(is_personal, login_url='usuario:login')

@login_required
def detalhe_avaliacao(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    return render(request, 'avaliacoes/detalhe_avaliacao.html', {'avaliacao': avaliacao})

@login_required
def lista_avaliacoes(request, aluno_id):
    aluno = get_object_or_404(Usuario, id=aluno_id)
    avaliacoes = Avaliacao.objects.filter(aluno=aluno)
    return render(request, 'avaliacoes/lista_avaliacoes.html', {'avaliacoes': avaliacoes, 'aluno': aluno})

@login_required
@personal_required
def cria_avaliacao(request, aluno_id):
    aluno = get_object_or_404(Usuario, id=aluno_id)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.profissional = request.user
            avaliacao.aluno = aluno
            avaliacao.save()
            return redirect('avaliacoes:lista_avaliacoes', aluno_id=aluno.id)
    else:
        form = AvaliacaoForm()
    return render(request, 'avaliacoes/cria_avaliacao.html', {'form': form, 'aluno': aluno})

@login_required
@personal_required
def atualiza_avaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('avaliacoes:lista_avaliacoes', aluno_id=avaliacao.aluno.id)
    else:
        form = AvaliacaoForm(instance=avaliacao)
    return render(request, 'avaliacoes/atualiza_avaliacao.html', {'form': form, 'avaliacao': avaliacao})

@login_required
@personal_required
def deleta_avaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)
    aluno_id = avaliacao.aluno.id
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('avaliacoes:lista_avaliacoes', aluno_id=aluno_id)
    return render(request, 'avaliacoes/deleta_avaliacao.html', {'avaliacao': avaliacao})
