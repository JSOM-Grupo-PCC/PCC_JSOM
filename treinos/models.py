from django.db import models
from django.conf import settings

class Treino(models.Model):
    personal = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='treinos_como_personal')
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='treinos_como_aluno')
    descricao = models.TextField()
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo