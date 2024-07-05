from django.db import models

class GrupoMuscular(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Exercicio(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='exercicios/', null=True, blank=True)
    grupo = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome