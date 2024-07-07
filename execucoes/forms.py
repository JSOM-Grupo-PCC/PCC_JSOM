# forms.py
from django import forms
from execucoes.models import Execucao

class ExecucaoForm(forms.ModelForm):
    class Meta:
        model = Execucao
        fields = ['serie', 'repeticoes', 'carga', 'exercicio']
