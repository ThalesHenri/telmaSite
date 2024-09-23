from django.db import models
from datetime import date

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(unique=True)
    telefone = models.IntegerField(unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=100, decimal_places=2)
    peso = models.DecimalField(max_digits=100, decimal_places=2)
    foto = models.ImageField(upload_to='Imagens_Produto/', blank=True, null=True)

    def __str__(self):
        return self.nome


class Compras(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valorPago = models.DecimalField(max_digits=100, decimal_places=2)
    pagamento = models.BooleanField(default=False)
    produtoComprado = models.ForeignKey(Produto, on_delete=models.CASCADE, default=1)
    quantidadeProdutos = models.IntegerField()
    dataCompra = models.DateField(default=date.today, blank=True, null=True)

    def __str__(self):
        return f"{self.cliente} >> {self.produtoComprado}"

    def save(self, *args, **kwargs):
        if self.pagamento:
            produto = self.produtoComprado
            if produto.quantidade >= self.quantidadeProdutos:
                produto.quantidade -= self.quantidadeProdutos
                produto.save()
            else:
                raise ValueError("Estoque insuficiente para completar a compra.")
        super().save(*args, **kwargs)