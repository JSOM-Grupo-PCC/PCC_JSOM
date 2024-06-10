from django.contrib import admin
from .models import Avaliacao

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('peso', 'altura', 'profissional', 'aluno', 'observacao')
    search_fields = ('profissional__username', 'aluno__username', 'observacao')
    list_filter = ('profissional', 'aluno')
