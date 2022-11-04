from django.shortcuts import render 
from django.db.models import Prefetch, Count
from .models import Processo

# Create your views here. 

def index(request):
    # O QuerySet é convertido para lista, para facilitar o debug.
    # Quando isso é feito, a consulta no banco é executada.
    query = Processo.objects\
        .annotate(qtd_tarefas=Count('tarefa'))\
        .annotate(qtd_funcionarios=Count('tarefa__funcionario'))\
        .prefetch_related(Prefetch('tarefa_set', to_attr='tarefas'))\
        .prefetch_related('tarefa_set__funcionario')
    processos = list(query)
    processos_colspans = zip(processos, [max(processo.qtd_tarefas, processo.qtd_funcionarios) for processo in processos])
    funcionarios = [tarefa.funcionario for processo in processos for tarefa in processo.tarefas]
    funcionarios_colspans = zip(funcionarios, [funcionario.tarefa_set.count() for funcionario in funcionarios])
    tarefas = [tarefa for processo in processos for tarefa in processo.tarefas]

    context = {
        'funcionarios_colspans': funcionarios_colspans,
        'tarefas': tarefas,
        'processos_colspans': processos_colspans
    }

    return render(request, 'teste/index.html', context)