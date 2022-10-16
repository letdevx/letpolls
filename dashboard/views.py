from http.client import HTTPResponse
from django.shortcuts import render
from .models import Etapa_Cliente

# Create your views here.
def index(request):
    clientes_etapas = Etapa_Cliente.objects.all()
    context = {
        'clientes_etapas': clientes_etapas
    }
    return render(request, 'dashboard/index.html', context)
