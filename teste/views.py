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
        .prefetch_related('tarefa_set__funcionario')\
        .order_by('ordem_processo')
    processos = list(query)
    # Descobre um colspan para cada processo, pegando sempre o maior (max)
    processos_colspans = zip(processos, [max(processo.qtd_tarefas, processo.qtd_funcionarios) for processo in processos])

    # Para cada processo, obtém uma lista de funcionarios não repetidos (à partir das tarefas do processo)
    funcionarios = []
    for processo in processos:
        funcionarios.extend(set([tarefa.funcionario for tarefa in processo.tarefas]))

    # Para cada processo, para cada funcionario do processo,
    # se o funcionario tem tarefas nesse processo, conta essas tarefas
    funcionarios_distintos = list(set(funcionarios)) # set elimina os repetidos
    colspans = []
    for processo in processos:
        colspans.extend([funcionario.tarefa_set.filter(processo__id=processo.id).count() for funcionario in funcionarios_distintos if funcionario.tarefa_set.filter(processo=processo)])
    funcionarios_colspans = zip(funcionarios, colspans)

    # Para cada processo, para cada tarefa no processo,
    # obtém as tarefas ordenadas por funcionario
    tarefas = [tarefa for processo in processos for tarefa in sorted(processo.tarefas, key=lambda t: t.funcionario_id)]

    context = {
        'processos_colspans': processos_colspans,
        'funcionarios_colspans': funcionarios_colspans,
        'tarefas': tarefas
    }

    return render(request, 'teste/index.html', context)