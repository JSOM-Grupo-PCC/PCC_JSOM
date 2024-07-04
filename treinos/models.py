from django.db import models
from exercicios.models import Exercicio
from programas.models import Programa

class Treino(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    serie = models.PositiveIntegerField()
    repeticoes = models.PositiveIntegerField()
    carga = models.FloatField()
    status = models.BooleanField(default=False)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Treino de {self.exercicio.nome} do Programa {self.programa.tipo}"