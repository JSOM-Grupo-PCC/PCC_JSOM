from django.contrib import admin
from .models import Treino

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'personal', 'aluno', 'descricao')
    search_fields = ('tipo', 'personal__username', 'aluno__username')
    list_filter = ('tipo',)
    ordering = ('tipo',)