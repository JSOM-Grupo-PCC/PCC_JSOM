from django.db import models
from exercicios.models import Exercicio
from programas.models import Treino

class Execucao(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    serie = models.PositiveIntegerField()
    repeticoes = models.PositiveIntegerField()
    carga = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.BooleanField(default=False)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Execução de {self.treino.descricao} - {self.serie}x{self.repeticoes}"