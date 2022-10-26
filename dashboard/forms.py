from django import forms

class CreateEtapaForm(forms.Form):
    descricao = forms.CharField(max_length=200)