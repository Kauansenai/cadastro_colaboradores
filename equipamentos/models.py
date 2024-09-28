from django.db import models

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField()
    quantidade_disponivel = models.PositiveIntegerField(default=0)  # Definir o valor padrão
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome