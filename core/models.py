from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    bairro = models.CharField(max_length=100)
    CEP = models.CharField(max_length=10)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=7)
    cpf = models.CharField(max_length=20, blank=True)
    cnpj = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.nome

class Estoque(models.Model):
    nome = models.CharField(max_length=100)
    qtd = models.SmallIntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrada = models.DateField(auto_now=True)
    data_vencimento = models.DateField()

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoque'

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valor_desconto = models.DecimalField(max_digits=10, decimal_places=2)
    pedido = models.TextField(max_length=1000)
    data_entrega = models.DateField()
    
    def total(self):
        return self.valor - self.valor_desconto
