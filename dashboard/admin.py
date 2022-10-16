from django.contrib import admin

# Register your models here.

from .models import Etapa, Etapa_Cliente, Cliente, Funcionario, Tarefa

admin.site.register(Etapa)
admin.site.register(Etapa_Cliente)
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Tarefa)