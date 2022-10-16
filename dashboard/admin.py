from django.contrib import admin

# Register your models here.

from .models import Etapa, Execucao, Cliente, Funcionario, Tarefa

admin.site.register(Etapa)
admin.site.register(Execucao)
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Tarefa)