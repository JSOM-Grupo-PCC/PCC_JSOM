from django.contrib import admin
from .models import Programa

class ExercicioInline(admin.TabularInline):
    model = Programa.exercicios.through
    extra = 1

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'personal', 'aluno', 'descricao')
    search_fields = ('tipo', 'personal__username', 'aluno__username')
    list_filter = ('tipo',)
    inlines = [ExercicioInline]
    ordering = ('tipo',)