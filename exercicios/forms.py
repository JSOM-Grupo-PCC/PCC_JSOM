from django import forms
from exercicios.models import GrupoMuscular, Exercicio

class GrupoMuscularForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2 text-white'}))
    class Meta:
        model = GrupoMuscular
        fields = ['nome']


class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['nome', 'descricao', 'grupo', 'imagem']
