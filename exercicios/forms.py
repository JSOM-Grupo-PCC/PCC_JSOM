from django import forms
from .models import GrupoMuscular

class GrupoMuscularForm(forms.ModelForm):
    class Meta:
        model = GrupoMuscular
        fields = ['nome']
