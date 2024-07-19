# avaliacoes/forms.py
from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['peso', 'altura', 'observacao']
        widgets = {
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'altura': forms.NumberInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }