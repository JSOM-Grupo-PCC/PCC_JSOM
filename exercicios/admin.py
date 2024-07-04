from django.contrib import admin
from .models import Exercicio, GrupoMuscular

@admin.register(GrupoMuscular)
class GrupoMuscularAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grupo')
    search_fields = ('nome', 'grupo__nome')
    list_filter = ('grupo',)
    ordering = ('nome',)