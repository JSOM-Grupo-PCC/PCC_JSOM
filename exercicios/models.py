from django.db import models

class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='exercicios_imagens/', blank=True, null=True)

    def __str__(self):
        return self.nome
