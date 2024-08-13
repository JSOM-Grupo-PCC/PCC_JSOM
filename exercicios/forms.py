from django import forms
from exercicios.models import GrupoMuscular, Exercicio

class GrupoMuscularForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    class Meta:
        model = GrupoMuscular
        fields = ['nome']


class ExercicioForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mb-2'}))
    grupo = forms.ModelChoiceField(queryset=GrupoMuscular.objects.all(), widget=forms.Select(attrs={'class': 'form-control mb-2'}))
    imagem = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-4', 'accept': 'image/*'}))
    
    class Meta:
        model = Exercicio
        fields = ['nome', 'descricao', 'grupo', 'imagem']