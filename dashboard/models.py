from django.db import models
from django.utils.translation import gettext_lazy as _

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

class Execucao(models.Model):
    class StatusExecucao(models.TextChoices):
        EMBARGADA = 'EMB', _('Embargada')
        INICIO_5A7_DIAS = '5A7', _('Inicio em 5 a 7 dias')
        INICIO_3A5_DIAS = '3A5', _('Inicio em 3 a 5 dias')
        INICIO_1A3_DIAS = '1A3', _('Inicio em 1 a 3 dias')
        INICIADA = 'INI', _('Já Iniciou')

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE) 
    status = models.CharField(
        max_length=3,
        choices=StatusExecucao.choices,
        default=StatusExecucao.INICIO_5A7_DIAS)
        
    def __str__(self):
        return f"{self.cliente.nome}-{self.tarefa.descricao}-{self.status}"