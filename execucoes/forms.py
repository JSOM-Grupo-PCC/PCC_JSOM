# forms.py
from django import forms
from execucoes.models import Execucao

class ExecucaoForm(forms.ModelForm):
    class Meta:
        model = Execucao
        fields = ['serie', 'repeticoes', 'carga', 'exercicio']
        widgets = {
            'serie': forms.TextInput(attrs={'class': 'form-control'}),
            'repeticoes': forms.NumberInput(attrs={'class': 'form-control'}),
            'carga': forms.NumberInput(attrs={'class': 'form-control'}),
            'exercicio': forms.Select(attrs={'class': 'form-control'}),
        }
