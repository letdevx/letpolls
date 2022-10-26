from django import forms
from .models import Etapa

class CreateEtapaForm(forms.Form):
    descricao = forms.CharField(max_length=200)

class CreateFuncionarioForm(forms.Form):
    nome = forms.CharField(max_length=200)
    etapa = forms.ModelChoiceField(queryset=Etapa.objects.all())