from django.db import models
from django.conf import settings

class Avaliacao(models.Model):
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    observacao = models.TextField(blank=True, null=True)
    profissional = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='avaliacoes_feitas', on_delete=models.CASCADE)
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='avaliacoes_recebidas', on_delete=models.CASCADE)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.aluno.username} por {self.profissional.username} em {self.data_avaliacao}"
