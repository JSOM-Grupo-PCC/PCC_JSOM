from django import forms
from exercicios.models import GrupoMuscular, Exercicio

class GrupoMuscularForm(forms.ModelForm):
    class Meta:
        model = GrupoMuscular
        fields = ['nome']

class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['nome', 'descricao', 'grupo', 'imagem']
