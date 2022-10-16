from http.client import HTTPResponse
from django.shortcuts import render
from .models import Etapa_Cliente, Cliente, Etapa

# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    etapas = Etapa.objects.all()
    clientes_etapas = Etapa_Cliente.objects.all()
    context = {
        'clientes': clientes,
        'etapas': etapas,
        'clientes_etapas': clientes_etapas
    }
    return render(request, 'dashboard/index.html', context)
