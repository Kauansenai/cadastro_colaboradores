from django.db import models
from colaboradores.models import Colaborador
from equipamentos.models import Equipamento

class Emprestimo(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.colaborador.nome} - {self.equipamento.nome}"
