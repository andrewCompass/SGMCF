from django.core.validators import MinValueValidator
from django.db import models

from pessoas.models import Afiliado

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Preço por Kg", verbose_name="Preço")

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3, default=0.000, help_text="Quantidade em Kg", verbose_name="Quantidade (Kg)", validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.produto.nome}"

class EstoqueIndividual(models.Model):

    class Meta:
        unique_together = ('produto', 'afiliado')
        verbose_name = "Estoque Individual"
        verbose_name_plural = "Estoques Individuais"

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    afiliado = models.ForeignKey(Afiliado, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3, default=0.000, help_text="Quantidade em Kg", verbose_name="Quantidade (Kg)", validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} Kg"

class HistoricoEstoque(models.Model):

    class Meta:
        verbose_name = "Histórico de Estoque"
        verbose_name_plural = "Histórico de Estoques"

    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('saida', 'Saída')], default='entrada')
    afiliado = models.ForeignKey(Afiliado, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=10, decimal_places=3, default=0.000, help_text="Peso em Kg", verbose_name="Peso")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.peso} Kg"