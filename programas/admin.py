from django.contrib import admin
from .models import Programa

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'tipo', 'personal', 'aluno')
    search_fields = ('descricao', 'tipo')
    list_filter = ('personal', 'aluno')
