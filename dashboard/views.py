from django.shortcuts import render
from django.db.models import Prefetch, Count
from .models import Cliente, Etapa, Funcionario, Tarefa

# Create your views here.
def index(request):
    clientes = Cliente.objects\
        .prefetch_related(Prefetch('execucao_set', to_attr='execucoes'))\
        .order_by('execucao__tarefa__id').all()
    etapas = Etapa.objects\
        .annotate(qtd_tarefas=Count('funcionario__tarefa'))\
        .order_by('id').all()
    funcionarios = Funcionario.objects\
        .annotate(qtd_tarefas=Count('tarefa'))\
        .order_by('etapa_id','id').all()
    tarefas = Tarefa.objects.order_by('funcionario_id','id').all()
    context = {
        'clientes': clientes,
        'etapas': etapas,
        'funcionarios': funcionarios,
        'tarefas': tarefas
    }
    return render(request, 'dashboard/index.html', context)
