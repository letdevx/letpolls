from django.db import models
from django.conf import settings

# Create your models here. 

class Processo (models.Model): 
    descricao = models.CharField(max_length=200) 
    ordem_processo = models.IntegerField()
    def __str__(self):
        return self.descricao 

class Tarefa(models.Model):
    descricao = models.CharField(max_length=200) 
    funcionario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    processo =  models.ForeignKey(Processo, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao 
