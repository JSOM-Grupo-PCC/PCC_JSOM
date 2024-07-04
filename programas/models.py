from django.db import models
from django.conf import settings
from exercicios.models import Exercicio

class Programa(models.Model):
    personal = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='programas_como_personal')
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='programas_como_aluno')
    exercicios = models.ManyToManyField(Exercicio)
    descricao = models.TextField()
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo