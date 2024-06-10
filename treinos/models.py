from django.db import models
from programas.models import Programa

class Treino(models.Model):
    serie = models.IntegerField()
    repeticoes = models.IntegerField()
    carga = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('pendente', 'Pendente'), ('completo', 'Completo')])
    exercicio = models.ForeignKey('exercicios.Exercicio', on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exercicio.nome} - {self.status}"
