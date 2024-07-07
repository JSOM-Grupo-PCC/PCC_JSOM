# forms.py
from django import forms
from treinos.models import Treino

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['descricao', 'tipo']
