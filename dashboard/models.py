from django.db import models

# Create your models here.

# Cliente ou Obra???
class Cliente(models.Model):
    nome = models.CharField(max_length=200)

class Etapa(models.Model):
    descricao = models.CharField(max_length=200)

class Etapa_Cliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)

class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)

class Tarefa(models.Model):
    descricao = models.CharField(max_length=200)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)