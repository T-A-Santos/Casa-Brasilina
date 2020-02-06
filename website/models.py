from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome, self.email, self.mensagem

