from django.contrib import admin
from .models import Treino

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('programa', 'exercicio', 'serie', 'repeticoes', 'carga', 'status')
    search_fields = ('programa__tipo', 'exercicio__nome')
    list_filter = ('status', 'programa__tipo')
    ordering = ('programa', 'exercicio')