from django.contrib import admin
from execucoes.models import Execucao

@admin.register(Execucao)
class ExecucaoAdmin(admin.ModelAdmin):
    list_display = ('treino', 'exercicio', 'serie', 'repeticoes', 'carga', 'status')
    search_fields = ('treino__tipo', 'exercicio__nome')
    list_filter = ('status', 'treino__tipo')
    ordering = ('treino', 'exercicio')