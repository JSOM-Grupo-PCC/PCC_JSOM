# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from exercicios.models import GrupoMuscular
from exercicios.forms import GrupoMuscularForm

def is_personal(user):
    return user.groups.filter(name="Personal").exists()

personal_required = user_passes_test(is_personal, login_url='usuario:login')

@personal_required
def grupo_muscular_list(request):
    grupos = GrupoMuscular.objects.all()
    return render(request, 'GruposMusculares/grupo_muscular_list.html', {'grupos': grupos})

@personal_required
def grupo_muscular_create(request):
    if request.method == 'POST':
        form = GrupoMuscularForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercicios:grupo_muscular_list')
    else:
        form = GrupoMuscularForm()
    return render(request, 'GruposMusculares/grupo_muscular_form.html', {'form': form})

@personal_required
def grupo_muscular_update(request, pk):
    grupo = get_object_or_404(GrupoMuscular, pk=pk)
    if request.method == 'POST':
        form = GrupoMuscularForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('exercicios:grupo_muscular_list')
    else:
        form = GrupoMuscularForm(instance=grupo)
    return render(request, 'GruposMusculares/grupo_muscular_form.html', {'form': form})

@personal_required
def grupo_muscular_delete(request, pk):
    grupo = get_object_or_404(GrupoMuscular, pk=pk)
    if request.method == 'POST':
        grupo.delete()
        return redirect('exercicios:grupo_muscular_list')
    return render(request, 'GruposMusculares/grupo_muscular_confirm_delete.html', {'grupo': grupo})
