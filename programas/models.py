from django.db import models
from django.conf import settings

class Programa(models.Model):
    descricao = models.TextField()
    tipo = models.CharField(max_length=100)
    personal = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='programas_criados', on_delete=models.CASCADE)
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='programas_inscritos', on_delete=models.CASCADE)
    exercicios = models.ManyToManyField('exercicios.Exercicio')

    def __str__(self):
        return self.descricao
