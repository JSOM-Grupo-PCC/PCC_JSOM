from django.contrib import admin
from .models import Treino

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('serie', 'repeticoes', 'carga', 'status', 'exercicio', 'programa')
    search_fields = ('status', 'exercicio__nome')
    list_filter = ('status', 'programa')
