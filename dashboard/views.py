from django.shortcuts import render
from django.db.models import Prefetch, Count
from django.http import HttpResponseRedirect
from .models import Cliente, Etapa, Funcionario, Tarefa
from .forms import CreateEtapaForm, CreateFuncionarioForm

# Create your views here.
def index(request):
    clientes = Cliente.objects\
        .prefetch_related(Prefetch('execucao_set', to_attr='execucoes'))\
        .order_by('execucao__tarefa__id').all()
    clientes_distintos = {cliente for cliente in clientes}
    etapas = Etapa.objects\
        .annotate(qtd_funcionarios=Count('funcionario'))\
        .annotate(qtd_tarefas=Count('funcionario__tarefa'))\
        .order_by('id').all()
    etapas_colspans = zip(etapas, [max(etapa.qtd_tarefas, etapa.qtd_funcionarios) for etapa in etapas])
    funcionarios = Funcionario.objects\
        .annotate(qtd_tarefas=Count('tarefa'))\
        .order_by('etapa_id','id').all()
    tarefas = Tarefa.objects.order_by('funcionario_id','id').all()
    context = {
        'clientes': clientes_distintos,
        'etapas_colspans': etapas_colspans,
        'funcionarios': funcionarios,
        'tarefas': tarefas
    }
    return render(request, 'dashboard/index.html', context)

def createEtapa(request):
    if request.method == 'POST':
        form = CreateEtapaForm(request.POST)
        if form.is_valid():
            etapa = Etapa(descricao=form.cleaned_data['descricao'])
            etapa.save()
            return HttpResponseRedirect('/dashboard')
    else:
        form = CreateEtapaForm()
    return render(request, 'dashboard/etapa_create.html', context={ 'form': form })

def createFuncionario(request):
    if request.method == 'POST':
        form = CreateFuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = Funcionario(nome=form.cleaned_data['nome'], etapa=form.cleaned_data['etapa'])
            funcionario.save()
            return HttpResponseRedirect('/dashboard')
    else:
        form = CreateFuncionarioForm()
    return render(request, 'dashboard/funcionario_create.html', context={ 'form': form })