from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    bairro = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=50, primary_key=True)


class Telefone(models.Model):
    telefone = models.CharField(max_length=20)
    descricao = models.CharField(max_length=70)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Estoque(models.Model):
    nome = models.CharField(max_length=100)
    qtd = models.SmallIntegerField()
    valor = models.SmallIntegerField()
    data_entrada = models.DateField(auto_now=True)


class Receita(models.Model) :
    receita = models.CharField(max_length=200)
    arquivo = models.FileField(blank=False, null=False)


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valor_desconto = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.TextField(max_length=1000, blank=True, null=True)
    data_entrega = models.DateField()
    entregue = models.BooleanField(blank=True, null=True)

    def total(self):
        return self.valor - self.valor_desconto

   