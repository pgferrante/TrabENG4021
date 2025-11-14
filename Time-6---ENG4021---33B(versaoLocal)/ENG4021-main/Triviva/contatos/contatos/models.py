from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} ({self.idade})"