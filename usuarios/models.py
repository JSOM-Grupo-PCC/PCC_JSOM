from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    data_nascimento = models.DateField(null=True, blank=True, editable=True)  
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
