from django.db import models


class Afiliado(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=15, blank=True, null=True, help_text="somente números")

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
