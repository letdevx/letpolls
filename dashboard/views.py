from http.client import HTTPResponse
from django.shortcuts import render
from .models import Execucao, Cliente, Etapa, Funcionario, Tarefa

# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    etapas = Etapa.objects.order_by('id').all()
    funcionarios = Funcionario.objects.order_by('etapa_id','id').all()
    tarefas = Tarefa.objects.order_by('funcionario_id','id').all()
    execucoes = Execucao.objects.all()
    context = {
        'clientes': clientes,
        'etapas': etapas,
        'funcionarios': funcionarios,
        'tarefas': tarefas,
        'execucoes': execucoes
    }
    return render(request, 'dashboard/index.html', context)
