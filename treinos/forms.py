# forms.py
from django import forms
from treinos.models import Treino

class TreinoForm(forms.ModelForm):
    TREINO_CHOICES = [
        ('Treino(A)', 'Treino(A)'),
        ('Treino(B)', 'Treino(B)'),
        ('Treino(C)', 'Treino(C)'),
        ('Treino(D)', 'Treino(D)'),
        ('Treino(E)', 'Treino(E)'),
        ('Treino(F)', 'Treino(F)'),
        ('Treino(G)', 'Treino(G)'),
    ]
    
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mb-2'}))
    tipo = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2', 
            'list': 'treino-options'  # Usando um data list para sugerir opções
        })
    )

    class Meta:
        model = Treino
        fields = ['descricao', 'tipo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo'].widget.attrs['placeholder'] = 'Escolha ou digite um tipo de treino'