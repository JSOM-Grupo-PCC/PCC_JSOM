from django.contrib import admin
from .models import Avaliacao

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('peso', 'altura', 'personal', 'aluno', 'observacao')
    search_fields = ('personal__username', 'aluno__username', 'observacao')
    list_filter = ('personal', 'aluno')
