# forms.py
from django import forms
from programas.models import Treino

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['descricao', 'tipo']
