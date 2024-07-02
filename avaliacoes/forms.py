# avaliacoes/forms.py
from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['peso', 'altura', 'observacao']
