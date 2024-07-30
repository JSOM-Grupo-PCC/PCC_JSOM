from django.db import models
from usuarios.models import Usuario

class Treino(models.Model):
    personal = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='treinos_como_personal')
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='treinos_como_aluno')
    descricao = models.TextField()
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo