from django.db import models

# Create your models here.

# Cliente ou Obra???
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Etapa(models.Model):
    descricao = models.CharField(max_length=200)
    def __str__(self):
        return self.descricao

class Etapa_Cliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.cliente.nome}-{self.etapa.descricao}"

class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    descricao = models.CharField(max_length=200)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao