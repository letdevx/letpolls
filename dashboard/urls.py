from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('etapas/create', views.createEtapa),
    path('funcionarios/create', views.createFuncionario)
]